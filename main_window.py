# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Sun Aug  4 00:18:28 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(678, 496)
        MainWindow.setMinimumSize(QtCore.QSize(500, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ps.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.main_splitter = QtGui.QSplitter(self.centralwidget)
        self.main_splitter.setOrientation(QtCore.Qt.Vertical)
        self.main_splitter.setOpaqueResize(True)
        self.main_splitter.setChildrenCollapsible(False)
        self.main_splitter.setObjectName(_fromUtf8("main_splitter"))
        self.splitter_2 = QtGui.QSplitter(self.main_splitter)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.board = QtGui.QGraphicsView(self.splitter_2)
        self.board.setMinimumSize(QtCore.QSize(200, 200))
        self.board.setObjectName(_fromUtf8("board"))
        self.run_groupbox = QtGui.QGroupBox(self.splitter_2)
        self.run_groupbox.setMinimumSize(QtCore.QSize(350, 245))
        self.run_groupbox.setMaximumSize(QtCore.QSize(350, 16777215))
        self.run_groupbox.setObjectName(_fromUtf8("run_groupbox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.run_groupbox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.run = QtGui.QToolButton(self.run_groupbox)
        self.run.setMinimumSize(QtCore.QSize(80, 0))
        self.run.setMaximumSize(QtCore.QSize(80, 16777215))
        self.run.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.run.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.run.setArrowType(QtCore.Qt.NoArrow)
        self.run.setObjectName(_fromUtf8("run"))
        self.gridLayout.addWidget(self.run, 2, 3, 1, 1)
        self.time_limit = QtGui.QSpinBox(self.run_groupbox)
        self.time_limit.setMinimum(1)
        self.time_limit.setMaximum(9999999)
        self.time_limit.setProperty("value", 60)
        self.time_limit.setObjectName(_fromUtf8("time_limit"))
        self.gridLayout.addWidget(self.time_limit, 2, 1, 1, 1)
        self.frame = QtGui.QFrame(self.run_groupbox)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout.addWidget(self.frame, 2, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.run_groupbox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.time_limit_label = QtGui.QLabel(self.run_groupbox)
        self.time_limit_label.setObjectName(_fromUtf8("time_limit_label"))
        self.gridLayout.addWidget(self.time_limit_label, 2, 0, 1, 1)
        self.methods_tree = QtGui.QTreeWidget(self.run_groupbox)
        self.methods_tree.setMinimumSize(QtCore.QSize(200, 100))
        self.methods_tree.setHeaderHidden(True)
        self.methods_tree.setObjectName(_fromUtf8("methods_tree"))
        self.methods_tree.headerItem().setText(0, _fromUtf8("1"))
        self.gridLayout.addWidget(self.methods_tree, 0, 0, 1, 4)
        self.neighborhood_list = QtGui.QListWidget(self.run_groupbox)
        self.neighborhood_list.setObjectName(_fromUtf8("neighborhood_list"))
        self.gridLayout.addWidget(self.neighborhood_list, 1, 1, 1, 3)
        self.gridLayout.setColumnMinimumWidth(0, 120)
        self.gridLayout.setRowStretch(0, 3)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tab_widget = QtGui.QTabWidget(self.main_splitter)
        self.tab_widget.setMinimumSize(QtCore.QSize(0, 130))
        self.tab_widget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tab_widget.setObjectName(_fromUtf8("tab_widget"))
        self.stat_tab = QtGui.QWidget()
        self.stat_tab.setObjectName(_fromUtf8("stat_tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.stat_tab)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.stat_table = QtGui.QTableWidget(self.stat_tab)
        self.stat_table.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stat_table.sizePolicy().hasHeightForWidth())
        self.stat_table.setSizePolicy(sizePolicy)
        self.stat_table.setMinimumSize(QtCore.QSize(0, 100))
        self.stat_table.setWordWrap(False)
        self.stat_table.setCornerButtonEnabled(False)
        self.stat_table.setColumnCount(7)
        self.stat_table.setObjectName(_fromUtf8("stat_table"))
        self.stat_table.setRowCount(0)
        self.stat_table.horizontalHeader().setHighlightSections(False)
        self.stat_table.horizontalHeader().setMinimumSectionSize(10)
        self.stat_table.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.stat_table)
        self.tab_widget.addTab(self.stat_tab, _fromUtf8(""))
        self.runtime_tab = QtGui.QWidget()
        self.runtime_tab.setObjectName(_fromUtf8("runtime_tab"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.runtime_tab)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.runtime_chart_frame = QtGui.QFrame(self.runtime_tab)
        self.runtime_chart_frame.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.runtime_chart_frame.setFrameShape(QtGui.QFrame.Box)
        self.runtime_chart_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.runtime_chart_frame.setLineWidth(0)
        self.runtime_chart_frame.setMidLineWidth(0)
        self.runtime_chart_frame.setObjectName(_fromUtf8("runtime_chart_frame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.runtime_chart_frame)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.runtime_chart = QtGui.QGraphicsView(self.runtime_chart_frame)
        self.runtime_chart.setFrameShape(QtGui.QFrame.NoFrame)
        self.runtime_chart.setLineWidth(0)
        self.runtime_chart.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.runtime_chart.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.runtime_chart.setObjectName(_fromUtf8("runtime_chart"))
        self.verticalLayout_3.addWidget(self.runtime_chart)
        self.horizontalLayout.addWidget(self.runtime_chart_frame)
        self.frame_2 = QtGui.QFrame(self.runtime_tab)
        self.frame_2.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(130, 16777215))
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.runtime_cost = QtGui.QLabel(self.frame_2)
        self.runtime_cost.setMinimumSize(QtCore.QSize(100, 0))
        self.runtime_cost.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.runtime_cost.setFont(font)
        self.runtime_cost.setStyleSheet(_fromUtf8("color: rgb(0, 127, 0);"))
        self.runtime_cost.setTextFormat(QtCore.Qt.AutoText)
        self.runtime_cost.setScaledContents(True)
        self.runtime_cost.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.runtime_cost.setObjectName(_fromUtf8("runtime_cost"))
        self.verticalLayout_4.addWidget(self.runtime_cost)
        self.best_cost_label = QtGui.QLabel(self.frame_2)
        self.best_cost_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.best_cost_label.setObjectName(_fromUtf8("best_cost_label"))
        self.verticalLayout_4.addWidget(self.best_cost_label)
        self.best_cost = QtGui.QLabel(self.frame_2)
        self.best_cost.setMinimumSize(QtCore.QSize(100, 0))
        self.best_cost.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.best_cost.setFont(font)
        self.best_cost.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.best_cost.setScaledContents(True)
        self.best_cost.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.best_cost.setObjectName(_fromUtf8("best_cost"))
        self.verticalLayout_4.addWidget(self.best_cost)
        self.horizontalLayout.addWidget(self.frame_2)
        self.tab_widget.addTab(self.runtime_tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.main_splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 678, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuProblem = QtGui.QMenu(self.menubar)
        self.menuProblem.setObjectName(_fromUtf8("menuProblem"))
        self.menuRun = QtGui.QMenu(self.menubar)
        self.menuRun.setObjectName(_fromUtf8("menuRun"))
        self.menuHistory = QtGui.QMenu(self.menubar)
        self.menuHistory.setObjectName(_fromUtf8("menuHistory"))
        self.menuImport = QtGui.QMenu(self.menuHistory)
        self.menuImport.setEnabled(False)
        self.menuImport.setObjectName(_fromUtf8("menuImport"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionGenerate_new = QtGui.QAction(MainWindow)
        self.actionGenerate_new.setObjectName(_fromUtf8("actionGenerate_new"))
        self.actionLoad_from_file = QtGui.QAction(MainWindow)
        self.actionLoad_from_file.setObjectName(_fromUtf8("actionLoad_from_file"))
        self.actionRestart = QtGui.QAction(MainWindow)
        self.actionRestart.setEnabled(False)
        self.actionRestart.setObjectName(_fromUtf8("actionRestart"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setEnabled(False)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionRun_once = QtGui.QAction(MainWindow)
        self.actionRun_once.setObjectName(_fromUtf8("actionRun_once"))
        self.actionRun_checked_methods = QtGui.QAction(MainWindow)
        self.actionRun_checked_methods.setObjectName(_fromUtf8("actionRun_checked_methods"))
        self.actionRun_all_methods = QtGui.QAction(MainWindow)
        self.actionRun_all_methods.setObjectName(_fromUtf8("actionRun_all_methods"))
        self.actionSave_history = QtGui.QAction(MainWindow)
        self.actionSave_history.setEnabled(False)
        self.actionSave_history.setObjectName(_fromUtf8("actionSave_history"))
        self.actionLoad_history = QtGui.QAction(MainWindow)
        self.actionLoad_history.setEnabled(False)
        self.actionLoad_history.setObjectName(_fromUtf8("actionLoad_history"))
        self.actionImportTo_CSV = QtGui.QAction(MainWindow)
        self.actionImportTo_CSV.setObjectName(_fromUtf8("actionImportTo_CSV"))
        self.actionClear = QtGui.QAction(MainWindow)
        self.actionClear.setEnabled(False)
        self.actionClear.setObjectName(_fromUtf8("actionClear"))
        self.actionDelete_selected = QtGui.QAction(MainWindow)
        self.actionDelete_selected.setEnabled(False)
        self.actionDelete_selected.setObjectName(_fromUtf8("actionDelete_selected"))
        self.actionStop = QtGui.QAction(MainWindow)
        self.actionStop.setEnabled(False)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))
        self.actionOptions = QtGui.QAction(MainWindow)
        self.actionOptions.setObjectName(_fromUtf8("actionOptions"))
        self.menuProblem.addAction(self.actionGenerate_new)
        self.menuProblem.addAction(self.actionLoad_from_file)
        self.menuProblem.addSeparator()
        self.menuProblem.addAction(self.actionSave)
        self.menuProblem.addSeparator()
        self.menuProblem.addAction(self.actionOptions)
        self.menuProblem.addAction(self.actionExit)
        self.menuRun.addAction(self.actionRun_once)
        self.menuRun.addAction(self.actionRun_checked_methods)
        self.menuRun.addAction(self.actionRun_all_methods)
        self.menuRun.addSeparator()
        self.menuRun.addAction(self.actionRestart)
        self.menuRun.addAction(self.actionStop)
        self.menuImport.addAction(self.actionImportTo_CSV)
        self.menuHistory.addAction(self.actionLoad_history)
        self.menuHistory.addAction(self.actionSave_history)
        self.menuHistory.addAction(self.menuImport.menuAction())
        self.menuHistory.addSeparator()
        self.menuHistory.addAction(self.actionClear)
        self.menuHistory.addAction(self.actionDelete_selected)
        self.menubar.addAction(self.menuProblem.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuHistory.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Problem Solver", None, QtGui.QApplication.UnicodeUTF8))
        self.run_groupbox.setTitle(QtGui.QApplication.translate("MainWindow", "Solving strategy", None, QtGui.QApplication.UnicodeUTF8))
        self.run.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Neighborhood:", None, QtGui.QApplication.UnicodeUTF8))
        self.time_limit_label.setText(QtGui.QApplication.translate("MainWindow", "Time limit, sec:", None, QtGui.QApplication.UnicodeUTF8))
        self.stat_table.setSortingEnabled(False)
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.stat_tab), QtGui.QApplication.translate("MainWindow", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Current avg. cost:", None, QtGui.QApplication.UnicodeUTF8))
        self.runtime_cost.setText(QtGui.QApplication.translate("MainWindow", "0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.best_cost_label.setText(QtGui.QApplication.translate("MainWindow", "Best found cost:", None, QtGui.QApplication.UnicodeUTF8))
        self.best_cost.setText(QtGui.QApplication.translate("MainWindow", "0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.runtime_tab), QtGui.QApplication.translate("MainWindow", "Runtime", None, QtGui.QApplication.UnicodeUTF8))
        self.menuProblem.setTitle(QtGui.QApplication.translate("MainWindow", "Problem", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRun.setTitle(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHistory.setTitle(QtGui.QApplication.translate("MainWindow", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.menuImport.setTitle(QtGui.QApplication.translate("MainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerate_new.setText(QtGui.QApplication.translate("MainWindow", "Generate new...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerate_new.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_from_file.setText(QtGui.QApplication.translate("MainWindow", "Load from file...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_from_file.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRestart.setText(QtGui.QApplication.translate("MainWindow", "Restart", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRestart.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun_once.setText(QtGui.QApplication.translate("MainWindow", "Run once", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun_once.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun_checked_methods.setText(QtGui.QApplication.translate("MainWindow", "Run checked methods", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun_checked_methods.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun_all_methods.setText(QtGui.QApplication.translate("MainWindow", "Run all methods", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_history.setText(QtGui.QApplication.translate("MainWindow", "Save history...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_history.setText(QtGui.QApplication.translate("MainWindow", "Load history...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImportTo_CSV.setText(QtGui.QApplication.translate("MainWindow", "to CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setText(QtGui.QApplication.translate("MainWindow", "Clear all", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_selected.setText(QtGui.QApplication.translate("MainWindow", "Delete selected", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setShortcut(QtGui.QApplication.translate("MainWindow", "Backspace", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOptions.setText(QtGui.QApplication.translate("MainWindow", "Options...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOptions.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))

