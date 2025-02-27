from pather import *
import trimesh
from stl import mesh
import subprocess
import time
import psutil
import matplotlib.pyplot as plt
import re
import matplotlib.transforms as transforms

def returnDimensions(mesh):
    min_coords, max_coords = mesh.bounds
    model_dimensions = max_coords - min_coords
    return model_dimensions

def generateSTL(points, filename, max_size):
    extrusion_height = 10
    extruded_mesh = trimesh.creation.extrude_polygon(Polygon(points), extrusion_height, engine="triangle")

    dimensions = returnDimensions(extruded_mesh) 
    scaling_factor = max_size / np.max(dimensions[:2])
    extruded_mesh.vertices *= np.array([scaling_factor, scaling_factor, 1])
    output_filename = f"{filename}_{scaling_factor:g}x"
    os.makedirs("stl", exist_ok=True)
    extruded_mesh.export(f'stl/{output_filename}.stl', file_type='stl')
    
    print(f"Model dimensions (mm): {dimensions}")
    print(f"New dimensions (mm): {dimensions*scaling_factor}")
    
    return extruded_mesh, output_filename

def killCuraengineProcesses():
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if 'CuraEngine.exe' in proc.info['name']:
                print(f"Killing process {proc.info['pid']}: {proc.info['name']}")
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

def extractGCode(gcode, rotation=180):
    with open(gcode, 'r') as f:
        lines = f.readlines()
    
    in_layer0 = False
    top_coords = []
    
    for line in lines:
        line = line.strip()
        if line.startswith(";LAYER_COUNT:"):
            layer_total = int(line.split(":")[1].strip())-1
        if line.startswith(";LAYER:"):
            layer_num = line.split(":")[1].strip()
            if layer_num == "0":
                in_layer0 = True
                continue
            elif in_layer0:
                break
                
        if in_layer0 and line.startswith("G"):
            match = re.search(r'X([-+]?[0-9]*\.?[0-9]+).*Y([-+]?[0-9]*\.?[0-9]+)', line)
            if match:
                x = float(match.group(1))
                y = float(match.group(2))
            if line.startswith("G1") and match:
                top_coords.append(("ON", x, y))
            if line.startswith("G0") and match:
                top_coords.append(("OFF", x, y))

    if in_layer0:
        name = os.path.basename(gcode)
        segments = []
        current_seg = []
        current_state = None
        
        _, x, y = zip(*top_coords)
        x = np.abs(x)
        y = np.abs(y)
        x -= np.min(x)
        y -= np.min(y)
        y -= np.max(y)
        x -= np.max(x)
        
        for index, (state, _, _) in enumerate(top_coords):
            xa = x[index]
            ya = y[index]
            if current_state is None:
                current_state = state
            if state == current_state:
                current_seg.append((xa, ya))
            else:
                segments.append((current_state, current_seg))
                current_state = state
                current_seg = [segments[-1][1][-1], (xa, ya)]
        if current_seg:
            segments.append((current_state, current_seg))
        
        plt.figure(figsize=(10, 10))

        trans = plt.gca().transData
        if rotation != 0:
            rot = transforms.Affine2D().rotate_deg(-rotation)
            trans = rot + plt.gca().transData
            
        
        for state, pts in segments:
            xs, ys = zip(*pts)
            if state == "ON":
                plt.plot(xs, ys, transform=trans, linewidth=1, color="blue")
            else:
                plt.plot(xs, ys, transform=trans, linewidth=1, color="red")
                
        plt.plot([], [], color="blue", label="ON")
        plt.plot([], [], color="red", label="OFF")
        
        plt.xlabel("X (mm)")
        plt.ylabel("Y (mm)")
        plt.title(f"State path for {name}")
        plt.grid(True)
        plt.legend(loc="best")
        plt.gca().set_aspect('equal')

        os.makedirs("plots", exist_ok=True)
        filename = os.path.splitext(name)[0]
        filename = os.path.basename(filename)
        plt.savefig(f'plots/{filename}.png',dpi=400,bbox_inches='tight')
        print(f"Saving {filename}.png to plots")
        
        plt.show()

    if not in_layer0:
        print("Error parsing gcode. No bottom layer detected.")

    return top_coords
    
def terminateAfterWriting(filename, process, check_interval=2, no_change_duration=10, plot=False):
    """
    Wait until the file's size stops changing for a given no_change_duration.
    """
    time_not_found=0
    while not os.path.exists(filename):
        print(f'Waiting {time_not_found:.2f} s',end='\r')
        if time_not_found >= 10:
            print(f"{filename} not found!")
            process.kill()
            try: 
                stdout, stderr = process.communicate()
            except Exception as e:
                print(e)
                return None, None, None
            if stderr != '':
                print(stderr)
            return stdout, stderr
        time.sleep(0.1)
        time_not_found+=0.1

    last_size = os.path.getsize(filename)
    print(f'(0 s) Watching "{filename}": {last_size} bytes'.ljust(200), end='\r')
    unchanged = 0
    t=0
    while unchanged < no_change_duration:
        time.sleep(check_interval)
        t+=check_interval
        current_size = os.path.getsize(filename)
        print(f'({t} s)  Checking "{filename}": {current_size} bytes'.ljust(200), end='\r')
        if current_size == last_size:
            unchanged += check_interval
        else:
            unchanged = 0
            last_size = current_size
    process.terminate()
    stdout, stderr = process.communicate()
    print(f'Process terminated after "{filename}" finished writing.\n')
    killCuraengineProcesses()

    coords = extractGCode(filename)
    file = os.path.splitext(filename)[0]
    file = os.path.basename(file)
    os.makedirs("paths", exist_ok=True)
    print(f"Saving {file}.txt to paths")
    with open(f'paths/{file}.txt', 'w') as f:
        for coord in coords:
            f.write(f'{coord}\n')

    return stdout, stderr, coords

def generateJSON(size, save=True):
    machine_def = f'''{{
        "version": 2,
        "name": "Path Generation ({size} mm)",
        "inherits": "fdmprinter",
        "metadata": {{
          "author": "Nolan Cummins",
          "file_formats": "text/x-gcode"
        }},
        "overrides": {{
          "extruder_nr": {{ "default_value": 0 }},
          "machine_nozzle_size": {{ "default_value": {size} }},
          "material_diameter": {{ "default_value": 1.75 }},
          "machine_name": {{ "default_value": "Pather" }},
          "layer_height": {{ "default_value": 0.4 }},
          "cool_min_layer_time_overhang": {{ "default_value": 5 }},
          "adhesion_type": {{ "default_value": "none" }},
          "skirt_line_count": {{ "default_value": 0 }},
          "brim_line_count": {{ "default_value": 0 }},
          "top_bottom_pattern_0": {{ "default_value": "zigzag" }},
          "acceleration_enabled": {{ "default_value": true }},
          "jerk_enabled": {{ "default_value": true }},
          "roofing_layer_count": {{ "default_value": 3 }},
          "support_enable": {{ "default_value": false }},
          "wall_line_count": {{ "default_value": 1 }},
          "min_wall_line_width": {{ "default_value": 0.0 }},
          "line_width": {{ "default_value": {size} }},
          "wall_line_width_0": {{ "default_value": {size} }},
          "wall_line_width_x": {{ "default_value": {size} }},
          "skin_line_width": {{ "default_value": {size} }},
          "infill_line_width": {{ "default_value": {size} }},
          "skirt_brim_line_width": {{ "default_value": {size} }},
          "support_line_width": {{ "default_value": {size} }},
          "support_interface_line_width": {{ "default_value": {size} }},
          "prime_tower_line_width": {{ "default_value": {size} }},
          "min_even_wall_line_width": {{ "default_value": 0.0 }},
          "min_odd_wall_line_width": {{ "default_value": 0.0 }},
          "min_bead_width": {{ "default_value": 0.0 }},
          "machine_nozzle_tip_outer_diameter": {{ "default_value": 0.0 }},
          "machine_nozzle_expansion_angle": {{ "default_value": 45 }},
          "xy_offset": {{ "default_value": 0.0 }},
          "xy_offset_layer_0": {{ "default_value": 0.0 }},
          "wall_0_inset": {{ "default_value": 0.0 }}
        }}
      }}'''

    os.makedirs("offsets", exist_ok=True)
    filepath = f"offsets/pather_{size}.def.json"
    if not os.path.isfile(filepath):
        with open(filepath, 'w') as f:
            f.write(machine_def)
            print(f"Saving pather_{size}.def.json")
            
    return machine_def

def runCura(cura_engine_path, machine_def_path, definitions_path, stl_path, output_path, wait=5, plot=False):
    os.environ["CURA_ENGINE_SEARCH_PATH"] = f"{definitions_path}"
    coords, result, command, stderr = None, None, None, None
    command = [
        cura_engine_path,
        "slice",
        "-v",
        "-j", machine_def_path,
        "-l", stl_path,
        "-o", output_path,
    ]

    killCuraengineProcesses()
    result = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, text=True)
    stdout, stderr, coords = terminateAfterWriting(output_path, result, no_change_duration=wait, plot=plot)
    
    return coords, result, command, stderr, stdout

