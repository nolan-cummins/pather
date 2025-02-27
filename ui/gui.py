# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiyySIka.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QStatusBar, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(914, 698)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.actionOpen.setIcon(icon)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.actionSave.setIcon(icon1)
        self.actionShow_Original = QAction(MainWindow)
        self.actionShow_Original.setObjectName(u"actionShow_Original")
        self.actionShow_Original.setCheckable(True)
        self.actionShow_Original.setChecked(True)
        self.actionHide_Image = QAction(MainWindow)
        self.actionHide_Image.setObjectName(u"actionHide_Image")
        self.actionHide_Image.setCheckable(True)
        self.actionAdaptive_Threshold = QAction(MainWindow)
        self.actionAdaptive_Threshold.setObjectName(u"actionAdaptive_Threshold")
        self.actionAdaptive_Threshold.setCheckable(True)
        self.actionAdaptive_Threshold.setChecked(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 500))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.outlinePlot = PlotWidget(self.frame)
        self.outlinePlot.setObjectName(u"outlinePlot")

        self.horizontalLayout_4.addWidget(self.outlinePlot)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 132))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.smoothSpinBox = QSpinBox(self.frame_2)
        self.smoothSpinBox.setObjectName(u"smoothSpinBox")
        self.smoothSpinBox.setMinimumSize(QSize(75, 21))
        self.smoothSpinBox.setMaximumSize(QSize(16777215, 21))
        self.smoothSpinBox.setMaximum(100)

        self.horizontalLayout_3.addWidget(self.smoothSpinBox)

        self.smoothSlider = QSlider(self.frame_2)
        self.smoothSlider.setObjectName(u"smoothSlider")
        self.smoothSlider.setMinimumSize(QSize(0, 21))
        self.smoothSlider.setMaximumSize(QSize(16777215, 30))
        self.smoothSlider.setMaximum(100)
        self.smoothSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_3.addWidget(self.smoothSlider)

        self.smoothLabel = QLabel(self.frame_2)
        self.smoothLabel.setObjectName(u"smoothLabel")
        self.smoothLabel.setMinimumSize(QSize(88, 21))
        self.smoothLabel.setMaximumSize(QSize(16777215, 30))
        self.smoothLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.smoothLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.simplifySpinBox = QSpinBox(self.frame_2)
        self.simplifySpinBox.setObjectName(u"simplifySpinBox")
        self.simplifySpinBox.setMinimumSize(QSize(75, 21))
        self.simplifySpinBox.setMaximumSize(QSize(16777215, 21))
        self.simplifySpinBox.setMaximum(100)

        self.horizontalLayout_5.addWidget(self.simplifySpinBox)

        self.simplifySlider = QSlider(self.frame_2)
        self.simplifySlider.setObjectName(u"simplifySlider")
        self.simplifySlider.setMinimumSize(QSize(0, 21))
        self.simplifySlider.setMaximumSize(QSize(16777215, 21))
        self.simplifySlider.setMaximum(100)
        self.simplifySlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_5.addWidget(self.simplifySlider)

        self.simplifyLabel = QLabel(self.frame_2)
        self.simplifyLabel.setObjectName(u"simplifyLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simplifyLabel.sizePolicy().hasHeightForWidth())
        self.simplifyLabel.setSizePolicy(sizePolicy)
        self.simplifyLabel.setMinimumSize(QSize(88, 21))
        self.simplifyLabel.setMaximumSize(QSize(16777215, 21))
        self.simplifyLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.simplifyLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.generatePathButton = QPushButton(self.frame_2)
        self.generatePathButton.setObjectName(u"generatePathButton")
        self.generatePathButton.setMinimumSize(QSize(300, 0))

        self.horizontalLayout.addWidget(self.generatePathButton)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.largestDim = QDoubleSpinBox(self.frame_2)
        self.largestDim.setObjectName(u"largestDim")
        self.largestDim.setMinimumSize(QSize(100, 0))
        self.largestDim.setMaximumSize(QSize(100, 16777215))
        self.largestDim.setMinimum(1.000000000000000)
        self.largestDim.setMaximum(100.000000000000000)

        self.horizontalLayout.addWidget(self.largestDim)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.diameter = QSpinBox(self.frame_2)
        self.diameter.setObjectName(u"diameter")
        self.diameter.setMinimumSize(QSize(100, 0))
        self.diameter.setMaximumSize(QSize(100, 16777215))
        self.diameter.setMinimum(10)
        self.diameter.setMaximum(1000)
        self.diameter.setValue(10)

        self.horizontalLayout.addWidget(self.diameter)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_6.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 914, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionShow_Original)
        self.menuEdit.addAction(self.actionHide_Image)
        self.menuEdit.addAction(self.actionAdaptive_Threshold)

        self.retranslateUi(MainWindow)
        self.smoothSlider.valueChanged.connect(self.smoothSpinBox.setValue)
        self.smoothSpinBox.valueChanged.connect(self.smoothSlider.setValue)
        self.simplifySlider.valueChanged.connect(self.simplifySpinBox.setValue)
        self.simplifySpinBox.valueChanged.connect(self.simplifySlider.setValue)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(whatsthis)
        self.actionOpen.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(whatsthis)
        self.actionSave.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.actionShow_Original.setText(QCoreApplication.translate("MainWindow", u"Show Original", None))
        self.actionHide_Image.setText(QCoreApplication.translate("MainWindow", u"Hide Image", None))
        self.actionAdaptive_Threshold.setText(QCoreApplication.translate("MainWindow", u"Adaptive Threshold", None))
        self.smoothLabel.setText(QCoreApplication.translate("MainWindow", u"Smooth Curve", None))
        self.simplifyLabel.setText(QCoreApplication.translate("MainWindow", u"Simplify Curve", None))
        self.generatePathButton.setText(QCoreApplication.translate("MainWindow", u"Generate Path", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Largest Dimension (mm)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Diameter (um)", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

