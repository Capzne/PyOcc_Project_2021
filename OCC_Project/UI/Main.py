# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import math

from OCC.Core.BOPAlgo import BOPAlgo_Splitter
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeRevol
from OCC.Core.GC import GC_MakeArcOfCircle, GC_MakeSegment
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Ax1, gp_Dir
from OCC.Extend.TopologyUtils import TopologyExplorer
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_test.qtDisplay import qtViewer3d
from OCC_Example import Elliptical


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1067, 711)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 125))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 161, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton_17 = QtWidgets.QToolButton(self.gridLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/3/newicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_17.setIcon(icon)
        self.toolButton_17.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_17.setObjectName("toolButton_17")
        self.gridLayout.addWidget(self.toolButton_17, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/3/openicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(30, 30))
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(self.gridLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icons/3/saveicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon2)
        self.toolButton_2.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout.addWidget(self.toolButton_2, 0, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(70, 80, 54, 12))
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(150, 10, 20, 70))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(180, 10, 148, 70))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.toolButton_12 = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./icons/4/o324412.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_12.setIcon(icon3)
        self.toolButton_12.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_12.setObjectName("toolButton_12")
        self.gridLayout_2.addWidget(self.toolButton_12, 1, 3, 1, 1)
        self.toolButton_11 = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./icons/4/o324408.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_11.setIcon(icon4)
        self.toolButton_11.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_11.setObjectName("toolButton_11")
        self.gridLayout_2.addWidget(self.toolButton_11, 0, 3, 1, 1)
        self.toolButton_6 = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./icons/4/o324409.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon5)
        self.toolButton_6.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_6.setObjectName("toolButton_6")
        self.gridLayout_2.addWidget(self.toolButton_6, 1, 0, 1, 1)
        self.toolButton_4 = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./icons/4/o324406.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon6)
        self.toolButton_4.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_4.setObjectName("toolButton_4")
        self.gridLayout_2.addWidget(self.toolButton_4, 0, 1, 1, 1)
        self.toolButton_7 = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./icons/4/o324410.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon7)
        self.toolButton_7.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_7.setObjectName("toolButton_7")
        self.gridLayout_2.addWidget(self.toolButton_7, 1, 1, 1, 1)
        self.toolButton_3 = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("./icons/4/o324405.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon8)
        self.toolButton_3.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_3.setObjectName("toolButton_3")
        self.gridLayout_2.addWidget(self.toolButton_3, 0, 0, 1, 1)
        self.toolButton_8 = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("./icons/4/o324411.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_8.setIcon(icon9)
        self.toolButton_8.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_8.setObjectName("toolButton_8")
        self.gridLayout_2.addWidget(self.toolButton_8, 1, 2, 1, 1)
        self.toolButton_5 = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("./icons/4/o324407.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon10)
        self.toolButton_5.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_5.setObjectName("toolButton_5")
        self.gridLayout_2.addWidget(self.toolButton_5, 0, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(330, 10, 20, 70))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(230, 80, 54, 12))
        self.label_4.setObjectName("label_4")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(360, 20, 92, 51))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.toolButton_10 = QtWidgets.QToolButton(self.gridLayoutWidget_3)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("./icons/6/codecalc2015_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_10.setIcon(icon11)
        self.toolButton_10.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_10.setObjectName("toolButton_10")
        self.gridLayout_3.addWidget(self.toolButton_10, 0, 1, 1, 1)
        self.toolButton_9 = QtWidgets.QToolButton(self.gridLayoutWidget_3)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("./icons/6/inputtabsicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_9.setIcon(icon12)
        self.toolButton_9.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_9.setObjectName("toolButton_9")
        self.gridLayout_3.addWidget(self.toolButton_9, 0, 0, 1, 1)
        self.toolButton_18 = QtWidgets.QToolButton(self.gridLayoutWidget_3)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("./icons/6/codecalcicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_18.setIcon(icon13)
        self.toolButton_18.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_18.setObjectName("toolButton_18")
        self.gridLayout_3.addWidget(self.toolButton_18, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(370, 80, 71, 12))
        self.label_5.setObjectName("label_5")
        self.line_3 = QtWidgets.QFrame(self.tab)
        self.line_3.setGeometry(QtCore.QRect(460, 10, 20, 70))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.tab)
        self.line_4.setGeometry(QtCore.QRect(570, 10, 20, 70))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.tab)
        self.line_5.setGeometry(QtCore.QRect(690, 10, 20, 70))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(500, 80, 54, 12))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(610, 80, 54, 12))
        self.label_7.setObjectName("label_7")
        self.line_6 = QtWidgets.QFrame(self.tab)
        self.line_6.setGeometry(QtCore.QRect(800, 10, 20, 70))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(740, 80, 54, 12))
        self.label_8.setObjectName("label_8")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(820, 0, 221, 74))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.gridLayout_4.addWidget(self.comboBox, 1, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_2, 0, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_4.addWidget(self.comboBox_3, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(900, 80, 81, 12))
        self.label_12.setObjectName("label_12")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(730, 10, 62, 60))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.toolButton_15 = QtWidgets.QToolButton(self.gridLayoutWidget_5)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("./icons/9/o322496.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_15.setIcon(icon14)
        self.toolButton_15.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_15.setObjectName("toolButton_15")
        self.gridLayout_5.addWidget(self.toolButton_15, 1, 0, 1, 1)
        self.toolButton_14 = QtWidgets.QToolButton(self.gridLayoutWidget_5)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("./icons/9/o322498.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_14.setIcon(icon15)
        self.toolButton_14.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_14.setObjectName("toolButton_14")
        self.gridLayout_5.addWidget(self.toolButton_14, 0, 1, 1, 1)
        self.toolButton_13 = QtWidgets.QToolButton(self.gridLayoutWidget_5)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("./icons/9/analyzeicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_13.setIcon(icon16)
        self.toolButton_13.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_13.setObjectName("toolButton_13")
        self.gridLayout_5.addWidget(self.toolButton_13, 0, 0, 1, 1)
        self.toolButton_16 = QtWidgets.QToolButton(self.gridLayoutWidget_5)
        self.toolButton_16.setIcon(icon15)
        self.toolButton_16.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_16.setObjectName("toolButton_16")
        self.gridLayout_5.addWidget(self.toolButton_16, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tabWidget.addTab(self.tab_11, "")
        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.dockWidget_2 = QtWidgets.QDockWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.dockWidget_2.sizePolicy().hasHeightForWidth())
        self.dockWidget_2.setSizePolicy(sizePolicy)
        self.dockWidget_2.setMaximumSize(QtCore.QSize(315, 524287))
        self.dockWidget_2.setFloating(False)
        self.dockWidget_2.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockWidget_2.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_2.setWindowTitle("")
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_2.setSizePolicy(sizePolicy)
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.dockWidgetContents_2)
        self.tabWidget_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tabWidget_2.setMaximumSize(QtCore.QSize(316, 524789))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tab_5.sizePolicy().hasHeightForWidth())
        self.tab_5.setSizePolicy(sizePolicy)
        self.tab_5.setObjectName("tab_5")
        self.toolBox_2 = QtWidgets.QToolBox(self.tab_5)
        self.toolBox_2.setGeometry(QtCore.QRect(0, 0, 311, 391))
        self.toolBox_2.setObjectName("toolBox_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 311, 339))
        self.page_3.setObjectName("page_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page_3)
        self.tableWidget_2.setEnabled(True)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 311, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setTabKeyNavigation(True)
        self.tableWidget_2.setProperty("showDropIndicator", True)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_2.setWordWrap(True)
        self.tableWidget_2.setCornerButtonEnabled(True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(18)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_2.verticalHeader().setVisible(True)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setHighlightSections(True)
        self.toolBox_2.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 311, 339))
        self.page_4.setObjectName("page_4")
        self.tableWidget = QtWidgets.QTableWidget(self.page_4)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 311, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.toolBox_2.addItem(self.page_4, "")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_5)
        self.plainTextEdit_2.setEnabled(False)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(0, 390, 311, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.gridLayout_7.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.gridLayout_7.setColumnStretch(0, 1)
        self.gridLayout_7.setRowStretch(0, 1)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        self.gridLayout_6.addWidget(self.dockWidget_2, 1, 0, 1, 1)
        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setRowStretch(0, 1)
        self.gridLayout_6.setRowStretch(1, 1)

        MainWindow.canva = qtViewer3d(self.centralwidget)
        MainWindow.canva.resize(720, 525)
        MainWindow.canva.move(330, 140)
        MainWindow.canva.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # 显示设置
        MainWindow.canva.InitDriver()  # canva的驱动,设置驱动后，才能成功display



        display = MainWindow.canva._display

        rgb_list1 = [206, 215, 222]
        rgb_list2 = [128, 128, 128]

        display.set_bg_gradient_color(rgb_list1, rgb_list2)  # 设置背景渐变色
        display.display_triedron()  # display black trihedron


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1067, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOutput = QtWidgets.QMenu(self.menubar)
        self.menuOutput.setObjectName("menuOutput")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOutput.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.toolBox_2.setCurrentIndex(0)


        #椭圆封头绘制
        Elli = Elliptical.Elliptical_Head()
        A = Elli.getElliptical_Head()
        display.DisplayShape(A.Shape(), update=True)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton_17.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Save"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Open"))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.label_13.setText(_translate("MainWindow", "New"))
        self.label_3.setText(_translate("MainWindow", "File"))
        self.toolButton_12.setText(_translate("MainWindow", "..."))
        self.toolButton_11.setText(_translate("MainWindow", "..."))
        self.toolButton_6.setText(_translate("MainWindow", "..."))
        self.toolButton_4.setText(_translate("MainWindow", "..."))
        self.toolButton_7.setText(_translate("MainWindow", "..."))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.toolButton_8.setText(_translate("MainWindow", "..."))
        self.toolButton_5.setText(_translate("MainWindow", "..."))
        self.label_4.setText(_translate("MainWindow", "Elements"))
        self.toolButton_10.setText(_translate("MainWindow", "..."))
        self.toolButton_9.setText(_translate("MainWindow", "..."))
        self.toolButton_18.setText(_translate("MainWindow", "..."))
        self.label_5.setText(_translate("MainWindow", "Input/Output"))
        self.label_6.setText(_translate("MainWindow", "Utility"))
        self.label_7.setText(_translate("MainWindow", "Auxiliary"))
        self.label_8.setText(_translate("MainWindow", "Analyse"))
        self.label_9.setText(_translate("MainWindow", "Design Code"))
        self.label_11.setText(_translate("MainWindow", "Div.2 Class"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Division1"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Inches"))
        self.label_10.setText(_translate("MainWindow", "Units"))
        self.label_12.setText(_translate("MainWindow", "Units/Code"))
        self.toolButton_15.setText(_translate("MainWindow", "..."))
        self.toolButton_14.setText(_translate("MainWindow", "..."))
        self.toolButton_13.setText(_translate("MainWindow", "..."))
        self.toolButton_16.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Home"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tools"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "View"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "3D"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Diagnostics"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "ESL"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), _translate("MainWindow", "Help"))
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "From Node"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "To Node"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Element Type"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Diameter Basis"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Inside Diameter"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Length"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Finished Thickness"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "Nominal Thickness"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "Internal Corrossion All"))
        item = self.tableWidget_2.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "External Corrosion All"))
        item = self.tableWidget_2.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "Wind Diameter Multiplier"))
        item = self.tableWidget_2.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "Material Name"))
        item = self.tableWidget_2.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "Longitudinal Seam Efficiency"))
        item = self.tableWidget_2.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "Circumferential Seam Efficiency"))
        item = self.tableWidget_2.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "Internal Pressure"))
        item = self.tableWidget_2.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "Temp. for Internal Pressure"))
        item = self.tableWidget_2.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "External Pressure"))
        item = self.tableWidget_2.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "Temp. for External Pressure"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Data"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_3), _translate("MainWindow", "Element Data"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Head Factor"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Inside Head Depth in                    "))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Sump Head"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Parent Nozzle"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Data"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_4), _translate("MainWindow", "Additional Element Data"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "General Input"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "Design Constraints"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "Load Cases"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("MainWindow", "Wind Data"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOutput.setTitle(_translate("MainWindow", "Output"))
