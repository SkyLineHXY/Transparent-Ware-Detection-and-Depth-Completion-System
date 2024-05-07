# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog/QT_source.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1176, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(1046, 912))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 1000))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 36px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_7.addWidget(self.line_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(174, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.imageButton = QtWidgets.QPushButton(self.centralwidget)
        self.imageButton.setMinimumSize(QtCore.QSize(55, 28))
        self.imageButton.setMaximumSize(QtCore.QSize(16777215, 28))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.imageButton.setFont(font)
        self.imageButton.setStyleSheet("QPushButton{\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color:rgb(50,50,50);\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(50, 50, 255, 0);\n"
"border-radius: 3px;\n"
"background-color: rgba(200, 200, 200,255);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 16px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(250,250,250);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 16px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(50,50,50);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(50, 50, 50, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/icon/打开.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imageButton.setIcon(icon)
        self.imageButton.setAutoRepeatInterval(100)
        self.imageButton.setObjectName("imageButton")
        self.verticalLayout_4.addWidget(self.imageButton)
        self.depthButton = QtWidgets.QPushButton(self.centralwidget)
        self.depthButton.setMinimumSize(QtCore.QSize(55, 28))
        self.depthButton.setMaximumSize(QtCore.QSize(16777215, 28))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.depthButton.setFont(font)
        self.depthButton.setStyleSheet("QPushButton{\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color:rgb(50,50,50);\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(50, 50, 255, 0);\n"
"border-radius: 3px;\n"
"background-color: rgba(200, 200, 200,1);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 16px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(250,250,250);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 16px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(50,50,50);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(50, 50, 50, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}")
        self.depthButton.setIcon(icon)
        self.depthButton.setObjectName("depthButton")
        self.verticalLayout_4.addWidget(self.depthButton)
        self.camButton = QtWidgets.QPushButton(self.centralwidget)
        self.camButton.setMinimumSize(QtCore.QSize(55, 28))
        self.camButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.camButton.setStyleSheet("QPushButton{font-family: \"Microsoft YaHei\";\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color:(50,50,50);\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(144,148,243,1);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 16px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(250,250,250);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 16px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/icon/摄像头开.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.camButton.setIcon(icon1)
        self.camButton.setObjectName("camButton")
        self.verticalLayout_4.addWidget(self.camButton)
        self.DepthcamButton = QtWidgets.QPushButton(self.centralwidget)
        self.DepthcamButton.setMinimumSize(QtCore.QSize(55, 28))
        self.DepthcamButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.DepthcamButton.setStyleSheet("QPushButton{font-family: \"Microsoft YaHei\";\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"color:(50,50,50);\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(144,243,144,1);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 16px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(250,250,250);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 16px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}")
        self.DepthcamButton.setIcon(icon1)
        self.DepthcamButton.setObjectName("DepthcamButton")
        self.verticalLayout_4.addWidget(self.DepthcamButton)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 28))
        self.label_5.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_5.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 12px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setMinimumSize(QtCore.QSize(0, 28))
        self.comboBox_2.setStyleSheet("QComboBox QAbstractItemView {\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 12px;\n"
"background:rgba(200, 200, 200,150);\n"
"selection-background-color: rgba(200, 200, 200,50);\n"
"color: rgb(50, 50, 50);\n"
"outline:none;\n"
"border:none;}\n"
"QComboBox{\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 12px;\n"
"color: rgb(50, 50, 50);\n"
"border-width:0px;\n"
"border-color:white;\n"
"border-style:solid;\n"
"background-color: rgba(200, 200, 200,0);}\n"
"\n"
"QComboBox::drop-down {\n"
"margin-top:8;\n"
"height:20;\n"
"background:rgba(255,255,255,0);\n"
"border-image: url(:/image/icon/下拉_白色.png);\n"
"}\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_2)
        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(0, 28))
        self.label_6.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_6.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 12px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setMinimumSize(QtCore.QSize(0, 28))
        self.comboBox_4.setStyleSheet("QComboBox QAbstractItemView {\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 12px;\n"
"background:rgba(200, 200, 200,150);\n"
"selection-background-color: rgba(200, 200, 200,50);\n"
"color: rgb(50, 50, 50);\n"
"outline:none;\n"
"border:none;}\n"
"QComboBox{\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 12px;\n"
"color: rgb(50, 50, 50);\n"
"border-width:0px;\n"
"border-color:white;\n"
"border-style:solid;\n"
"background-color: rgba(200, 200, 200,0);}\n"
"\n"
"QComboBox::drop-down {\n"
"margin-top:8;\n"
"height:20;\n"
"background:rgba(255,255,255,0);\n"
"border-image: url(:/image/icon/下拉_白色.png);\n"
"}\n"
"")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMinimumSize(QtCore.QSize(0, 28))
        self.label_7.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_7.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 12px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setMinimumSize(QtCore.QSize(0, 28))
        self.comboBox_3.setStyleSheet("QComboBox QAbstractItemView {\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 12px;\n"
"background:rgba(200, 200, 200,50);\n"
"selection-background-color: rgba(200, 200, 200,50);\n"
"color: rgb(80, 50, 50);\n"
"outline:none;\n"
"border:none;}\n"
"QComboBox{\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 12px;\n"
"color: rgb(50, 50, 50);\n"
"border-width:0px;\n"
"border-color:white;\n"
"border-style:solid;\n"
"background-color: rgba(200, 200, 200,0);}\n"
"\n"
"QComboBox::drop-down {\n"
"margin-top:8;\n"
"height:20;\n"
"background:rgba(255,255,255,0);\n"
"border-image: url(:/image/icon/下拉_白色.png);\n"
"}\n"
"")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_3)
        self.horizontalLayout_6.setStretch(0, 3)
        self.horizontalLayout_6.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(174, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_8.addWidget(self.line_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_depth_in = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_depth_in.setFont(font)
        self.label_depth_in.setStyleSheet("background-color: rgba(0, 0, 0, 255);")
        self.label_depth_in.setText("")
        self.label_depth_in.setScaledContents(False)
        self.label_depth_in.setObjectName("label_depth_in")
        self.horizontalLayout_2.addWidget(self.label_depth_in)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_2.addWidget(self.line_6)
        self.label_rgb_in = QtWidgets.QLabel(self.centralwidget)
        self.label_rgb_in.setStyleSheet("background-color: rgba(0, 0, 0, 255);")
        self.label_rgb_in.setObjectName("label_rgb_in")
        self.horizontalLayout_2.addWidget(self.label_rgb_in)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(2, 7)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_7.addWidget(self.line_3)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 36px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_8.addWidget(self.line_7)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 24px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_2.addWidget(self.line_5)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_11.addLayout(self.verticalLayout_2)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_11.addWidget(self.line_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_depth_out = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_depth_out.setFont(font)
        self.label_depth_out.setStyleSheet("background-color: rgba(0, 0, 0, 255);")
        self.label_depth_out.setText("")
        self.label_depth_out.setScaledContents(False)
        self.label_depth_out.setObjectName("label_depth_out")
        self.verticalLayout_3.addWidget(self.label_depth_out)
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout_3.addWidget(self.line_11)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_surf_out = QtWidgets.QLabel(self.centralwidget)
        self.label_surf_out.setStyleSheet("background-color: rgba(0, 0, 0, 255);")
        self.label_surf_out.setObjectName("label_surf_out")
        self.horizontalLayout_9.addWidget(self.label_surf_out)
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.horizontalLayout_9.addWidget(self.line_10)
        self.label_outline_out = QtWidgets.QLabel(self.centralwidget)
        self.label_outline_out.setStyleSheet("background-color: rgba(0, 0, 0, 255);")
        self.label_outline_out.setObjectName("label_outline_out")
        self.horizontalLayout_9.addWidget(self.label_outline_out)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.label_rgb_out = QtWidgets.QLabel(self.centralwidget)
        self.label_rgb_out.setStyleSheet("background-color: rgba(0, 0, 0, 255);")
        self.label_rgb_out.setObjectName("label_rgb_out")
        self.horizontalLayout_3.addWidget(self.label_rgb_out)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(2, 2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_6.addWidget(self.line_2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 81, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 81, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 81, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.resetButton.setPalette(palette)
        self.resetButton.setStyleSheet("QPushButton{font-family: \"Microsoft YaHei\";\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"font-color: (0, 50, 50)\n"
"color:white;\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(255, 255, 255,1);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(225, 205, 205, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 20px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(250,250,250);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}")
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_10.addWidget(self.resetButton)
        self.RunButton = QtWidgets.QPushButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 81, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 81, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 81, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.RunButton.setPalette(palette)
        self.RunButton.setStyleSheet("QPushButton{font-family: \"Microsoft YaHei\";\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"font-color: (0, 50, 50)\n"
"color:white;\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(255, 255, 255,1);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(225, 205, 205, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 20px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(250,250,250);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:rgb(250,200,0);}")
        self.RunButton.setObjectName("RunButton")
        self.horizontalLayout_10.addWidget(self.RunButton)
        self.RunButton_2 = QtWidgets.QPushButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 81, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 81, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 81, 59))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.RunButton_2.setPalette(palette)
        self.RunButton_2.setStyleSheet("QPushButton{font-family: \"Microsoft YaHei\";\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"font-color: (0, 50, 50)\n"
"color:white;\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(255, 255, 255,1);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(225, 205, 205, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 20px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(250,250,250);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:#7efd08;}")
        self.RunButton_2.setObjectName("RunButton_2")
        self.horizontalLayout_10.addWidget(self.RunButton_2)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setStyleSheet("QPushButton{font-family: \"Microsoft YaHei\";\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"font-color: (0, 50, 50)\n"
"color:white;\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(255, 255, 255,1);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(225, 205, 205, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 20px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(250,250,250);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:#7efd08;}")
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_10.addWidget(self.saveButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.verticalLayout_6.setStretch(0, 10)
        self.horizontalLayout_11.addLayout(self.verticalLayout_6)
        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(2, 7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        self.verticalLayout_7.setStretch(2, 2)
        self.verticalLayout_7.setStretch(4, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1176, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Input"))
        self.imageButton.setToolTip(_translate("MainWindow", "file"))
        self.imageButton.setText(_translate("MainWindow", "RGB"))
        self.depthButton.setToolTip(_translate("MainWindow", "file"))
        self.depthButton.setText(_translate("MainWindow", "Depth"))
        self.camButton.setToolTip(_translate("MainWindow", "camera"))
        self.camButton.setText(_translate("MainWindow", "Cam"))
        self.DepthcamButton.setToolTip(_translate("MainWindow", "camera"))
        self.DepthcamButton.setText(_translate("MainWindow", "RGB_Cam"))
        self.label_5.setText(_translate("MainWindow", "nor_model"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "R50"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "DRN"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "ViT"))
        self.label_6.setText(_translate("MainWindow", "mask_model"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "R50"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "DRN"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "ViT"))
        self.label_7.setText(_translate("MainWindow", "det_model"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "R50-FPN"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "R50-CBAM-FPN"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "R50-CBAM"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "R50"))
        self.label_rgb_in.setText(_translate("MainWindow", "2"))
        self.label.setText(_translate("MainWindow", "Result"))
        self.label_2.setText(_translate("MainWindow", "Metrics"))
        self.label_surf_out.setText(_translate("MainWindow", "2"))
        self.label_outline_out.setText(_translate("MainWindow", "2"))
        self.label_rgb_out.setText(_translate("MainWindow", "2"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.RunButton.setText(_translate("MainWindow", "Complition"))
        self.RunButton_2.setText(_translate("MainWindow", "Detect"))
        self.saveButton.setText(_translate("MainWindow", "Save figure"))
from dialog import pictures_rc
