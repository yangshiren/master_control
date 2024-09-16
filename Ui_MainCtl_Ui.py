# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainCtl_Ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextBrowser,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1391, 946)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_11 = QGridLayout(self.tab_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tableWidget_Results = QTableWidget(self.tab_3)
        if (self.tableWidget_Results.columnCount() < 10):
            self.tableWidget_Results.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget_Results.setObjectName(u"tableWidget_Results")
        self.tableWidget_Results.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_Results.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_Results.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_11.addWidget(self.tableWidget_Results, 2, 0, 1, 1)

        self.frame_3 = QFrame(self.tab_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_3)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.groupBox = QGroupBox(self.frame_3)
        self.groupBox.setObjectName(u"groupBox")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"")
        self.gridLayout_9 = QGridLayout(self.groupBox)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_9.addWidget(self.radioButton, 0, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_9.addWidget(self.radioButton_2, 1, 0, 1, 1)

        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_9.addWidget(self.radioButton_3, 2, 0, 1, 1)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_9.addWidget(self.checkBox, 3, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox, 0, 0, 3, 1)

        self.groupBox_status = QGroupBox(self.frame_3)
        self.groupBox_status.setObjectName(u"groupBox_status")
        self.groupBox_status.setFont(font1)
        self.verticalLayout = QVBoxLayout(self.groupBox_status)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.status_live = QToolButton(self.groupBox_status)
        self.status_live.setObjectName(u"status_live")
        self.status_live.setFont(font1)
        self.status_live.setAutoFillBackground(False)
        self.status_live.setStyleSheet(u"background:rgb(0, 255, 0)")
        self.status_live.setPopupMode(QToolButton.DelayedPopup)
        self.status_live.setAutoRaise(True)

        self.verticalLayout.addWidget(self.status_live)

        self.status_road = QToolButton(self.groupBox_status)
        self.status_road.setObjectName(u"status_road")
        self.status_road.setFont(font1)
        self.status_road.setAutoFillBackground(False)
        self.status_road.setStyleSheet(u"background:rgb(0, 255, 0)")
        self.status_road.setPopupMode(QToolButton.DelayedPopup)
        self.status_road.setAutoRaise(True)
        self.status_road.setArrowType(Qt.NoArrow)

        self.verticalLayout.addWidget(self.status_road)

        self.status_lenses = QToolButton(self.groupBox_status)
        self.status_lenses.setObjectName(u"status_lenses")
        self.status_lenses.setFont(font1)
        self.status_lenses.setAutoFillBackground(False)
        self.status_lenses.setStyleSheet(u"background:rgb(0, 255, 0)")
        self.status_lenses.setPopupMode(QToolButton.DelayedPopup)
        self.status_lenses.setAutoRaise(True)

        self.verticalLayout.addWidget(self.status_lenses)

        self.status_track = QToolButton(self.groupBox_status)
        self.status_track.setObjectName(u"status_track")
        self.status_track.setFont(font1)
        self.status_track.setAutoFillBackground(False)
        self.status_track.setStyleSheet(u"background:rgb(0, 255, 0)")
        self.status_track.setPopupMode(QToolButton.DelayedPopup)
        self.status_track.setAutoRaise(True)

        self.verticalLayout.addWidget(self.status_track)


        self.gridLayout_12.addWidget(self.groupBox_status, 0, 1, 3, 1)

        self.groupBox_status_2 = QGroupBox(self.frame_3)
        self.groupBox_status_2.setObjectName(u"groupBox_status_2")
        self.groupBox_status_2.setMaximumSize(QSize(375, 16777215))
        self.groupBox_status_2.setFont(font1)
        self.gridLayout_3 = QGridLayout(self.groupBox_status_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.status_server1 = QToolButton(self.groupBox_status_2)
        self.status_server1.setObjectName(u"status_server1")
        self.status_server1.setFont(font1)
        self.status_server1.setAutoFillBackground(False)
        self.status_server1.setStyleSheet(u"background:rgb(255, 0, 0)")
        self.status_server1.setPopupMode(QToolButton.DelayedPopup)
        self.status_server1.setAutoRaise(True)
        self.status_server1.setArrowType(Qt.NoArrow)

        self.gridLayout_3.addWidget(self.status_server1, 0, 0, 1, 2)

        self.status_server2 = QToolButton(self.groupBox_status_2)
        self.status_server2.setObjectName(u"status_server2")
        self.status_server2.setFont(font1)
        self.status_server2.setAutoFillBackground(False)
        self.status_server2.setStyleSheet(u"background:rgb(255, 0, 0)")
        self.status_server2.setPopupMode(QToolButton.DelayedPopup)
        self.status_server2.setAutoRaise(True)

        self.gridLayout_3.addWidget(self.status_server2, 0, 2, 1, 2)

        self.status_sportsCards = QToolButton(self.groupBox_status_2)
        self.status_sportsCards.setObjectName(u"status_sportsCards")
        self.status_sportsCards.setFont(font1)
        self.status_sportsCards.setAutoFillBackground(False)
        self.status_sportsCards.setStyleSheet(u"background:rgb(0, 255, 0)")
        self.status_sportsCards.setPopupMode(QToolButton.DelayedPopup)
        self.status_sportsCards.setAutoRaise(True)

        self.gridLayout_3.addWidget(self.status_sportsCards, 0, 4, 1, 2)

        self.frame_4 = QFrame(self.groupBox_status_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(70, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_4, 0, 6, 2, 1)

        self.status_obs = QToolButton(self.groupBox_status_2)
        self.status_obs.setObjectName(u"status_obs")
        self.status_obs.setFont(font1)
        self.status_obs.setAutoFillBackground(False)
        self.status_obs.setStyleSheet(u"background:rgb(0, 255, 0)")
        self.status_obs.setPopupMode(QToolButton.DelayedPopup)
        self.status_obs.setAutoRaise(True)

        self.gridLayout_3.addWidget(self.status_obs, 1, 0, 1, 1)

        self.status_mainlenses = QToolButton(self.groupBox_status_2)
        self.status_mainlenses.setObjectName(u"status_mainlenses")
        self.status_mainlenses.setFont(font1)
        self.status_mainlenses.setAutoFillBackground(False)
        self.status_mainlenses.setStyleSheet(u"background:rgb(0, 255, 0)")
        self.status_mainlenses.setPopupMode(QToolButton.DelayedPopup)
        self.status_mainlenses.setAutoRaise(True)

        self.gridLayout_3.addWidget(self.status_mainlenses, 1, 1, 1, 2)

        self.status_Recognition = QToolButton(self.groupBox_status_2)
        self.status_Recognition.setObjectName(u"status_Recognition")
        self.status_Recognition.setFont(font1)
        self.status_Recognition.setAutoFillBackground(False)
        self.status_Recognition.setStyleSheet(u"background:rgb(255, 0, 0)")
        self.status_Recognition.setPopupMode(QToolButton.DelayedPopup)
        self.status_Recognition.setAutoRaise(True)

        self.gridLayout_3.addWidget(self.status_Recognition, 1, 3, 1, 2)

        self.status_Extension = QToolButton(self.groupBox_status_2)
        self.status_Extension.setObjectName(u"status_Extension")
        self.status_Extension.setFont(font1)
        self.status_Extension.setAutoFillBackground(False)
        self.status_Extension.setStyleSheet(u"background:rgb(0, 255, 0)")
        self.status_Extension.setPopupMode(QToolButton.DelayedPopup)
        self.status_Extension.setAutoRaise(True)

        self.gridLayout_3.addWidget(self.status_Extension, 1, 5, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_status_2, 0, 2, 1, 1)

        self.groupBox_3 = QGroupBox(self.frame_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font1)
        self.gridLayout_16 = QGridLayout(self.groupBox_3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.checkBox_2 = QCheckBox(self.groupBox_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font1)

        self.gridLayout_16.addWidget(self.checkBox_2, 0, 0, 1, 1)

        self.checkBox_7 = QCheckBox(self.groupBox_3)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setFont(font1)

        self.gridLayout_16.addWidget(self.checkBox_7, 0, 1, 1, 1)

        self.checkBox_3 = QCheckBox(self.groupBox_3)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font1)

        self.gridLayout_16.addWidget(self.checkBox_3, 1, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.groupBox_3)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setFont(font1)

        self.gridLayout_16.addWidget(self.checkBox_4, 1, 1, 1, 1)

        self.checkBox_6 = QCheckBox(self.groupBox_3)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setFont(font1)

        self.gridLayout_16.addWidget(self.checkBox_6, 2, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.groupBox_3)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setFont(font1)

        self.gridLayout_16.addWidget(self.checkBox_5, 2, 1, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_3, 0, 3, 2, 2)

        self.groupBox_2 = QGroupBox(self.frame_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(375, 16777215))
        self.groupBox_2.setFont(font1)
        self.gridLayout_8 = QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.lineEdit_4 = QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_8.addWidget(self.lineEdit_4, 0, 2, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_8.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_8.addWidget(self.lineEdit_3, 0, 3, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_8.addWidget(self.lineEdit_2, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.groupBox_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(50, 0))
        self.frame_5.setMaximumSize(QSize(100, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout_8.addWidget(self.frame_5, 0, 4, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_2, 1, 2, 2, 1)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 50))
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)

        self.gridLayout_12.addWidget(self.pushButton, 2, 3, 1, 1)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_17.addWidget(self.label_2, 0, 3, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(30, 16777215))
        self.lineEdit_5.setReadOnly(True)

        self.gridLayout_17.addWidget(self.lineEdit_5, 0, 2, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(85, 16777215))
        self.label.setFont(font1)
        self.label.setAutoFillBackground(False)

        self.gridLayout_17.addWidget(self.label, 0, 1, 1, 1)


        self.gridLayout_12.addWidget(self.frame, 2, 4, 1, 1)


        self.gridLayout_11.addWidget(self.frame_3, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.tab_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 0))
        self.frame_2.setMaximumSize(QSize(380, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_add_3 = QPushButton(self.frame_8)
        self.pushButton_add_3.setObjectName(u"pushButton_add_3")
        self.pushButton_add_3.setMaximumSize(QSize(200, 16777215))
        self.pushButton_add_3.setFont(font1)
        self.pushButton_add_3.setStyleSheet(u"background:rgb(255, 0, 0)")

        self.horizontalLayout_2.addWidget(self.pushButton_add_3)

        self.pushButton_start_2 = QPushButton(self.frame_8)
        self.pushButton_start_2.setObjectName(u"pushButton_start_2")
        self.pushButton_start_2.setMaximumSize(QSize(200, 16777215))
        self.pushButton_start_2.setFont(font1)
        self.pushButton_start_2.setStyleSheet(u"background:rgb(255, 255, 0)")

        self.horizontalLayout_2.addWidget(self.pushButton_start_2)


        self.gridLayout_10.addWidget(self.frame_8, 0, 0, 1, 1)

        self.textBrowser_msg = QTextBrowser(self.frame_2)
        self.textBrowser_msg.setObjectName(u"textBrowser_msg")

        self.gridLayout_10.addWidget(self.textBrowser_msg, 4, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_add_2 = QPushButton(self.frame_7)
        self.pushButton_add_2.setObjectName(u"pushButton_add_2")

        self.gridLayout_7.addWidget(self.pushButton_add_2, 0, 0, 1, 1)

        self.pushButton_save_2 = QPushButton(self.frame_7)
        self.pushButton_save_2.setObjectName(u"pushButton_save_2")
        self.pushButton_save_2.setMinimumSize(QSize(20, 0))
        self.pushButton_save_2.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_save_2, 0, 1, 1, 1)

        self.pushButton_update_2 = QPushButton(self.frame_7)
        self.pushButton_update_2.setObjectName(u"pushButton_update_2")
        self.pushButton_update_2.setMinimumSize(QSize(20, 0))
        self.pushButton_update_2.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_update_2, 0, 2, 1, 1)

        self.pushButton_save_3 = QPushButton(self.frame_7)
        self.pushButton_save_3.setObjectName(u"pushButton_save_3")
        self.pushButton_save_3.setMinimumSize(QSize(20, 0))
        self.pushButton_save_3.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_save_3, 0, 3, 1, 1)

        self.pushButton_update_3 = QPushButton(self.frame_7)
        self.pushButton_update_3.setObjectName(u"pushButton_update_3")
        self.pushButton_update_3.setMinimumSize(QSize(20, 0))
        self.pushButton_update_3.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_update_3, 0, 4, 1, 1)

        self.pushButton_save_4 = QPushButton(self.frame_7)
        self.pushButton_save_4.setObjectName(u"pushButton_save_4")
        self.pushButton_save_4.setMinimumSize(QSize(20, 0))
        self.pushButton_save_4.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_save_4, 0, 5, 1, 1)

        self.pushButton_update_5 = QPushButton(self.frame_7)
        self.pushButton_update_5.setObjectName(u"pushButton_update_5")
        self.pushButton_update_5.setMinimumSize(QSize(20, 0))
        self.pushButton_update_5.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_update_5, 0, 6, 1, 1)

        self.pushButton_save_5 = QPushButton(self.frame_7)
        self.pushButton_save_5.setObjectName(u"pushButton_save_5")
        self.pushButton_save_5.setMinimumSize(QSize(20, 0))
        self.pushButton_save_5.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_save_5, 0, 7, 1, 1)

        self.pushButton_update_4 = QPushButton(self.frame_7)
        self.pushButton_update_4.setObjectName(u"pushButton_update_4")
        self.pushButton_update_4.setMinimumSize(QSize(20, 0))
        self.pushButton_update_4.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_update_4, 0, 8, 1, 1)

        self.pushButton_save_6 = QPushButton(self.frame_7)
        self.pushButton_save_6.setObjectName(u"pushButton_save_6")
        self.pushButton_save_6.setMinimumSize(QSize(20, 0))
        self.pushButton_save_6.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_save_6, 0, 9, 1, 1)

        self.pushButton_update_6 = QPushButton(self.frame_7)
        self.pushButton_update_6.setObjectName(u"pushButton_update_6")
        self.pushButton_update_6.setMinimumSize(QSize(30, 0))
        self.pushButton_update_6.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_update_6, 0, 10, 1, 1)

        self.pushButton_once_2 = QPushButton(self.frame_7)
        self.pushButton_once_2.setObjectName(u"pushButton_once_2")

        self.gridLayout_7.addWidget(self.pushButton_once_2, 1, 0, 1, 1)

        self.pushButton_save_7 = QPushButton(self.frame_7)
        self.pushButton_save_7.setObjectName(u"pushButton_save_7")
        self.pushButton_save_7.setMinimumSize(QSize(20, 0))
        self.pushButton_save_7.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_save_7, 1, 1, 1, 1)

        self.pushButton_update_10 = QPushButton(self.frame_7)
        self.pushButton_update_10.setObjectName(u"pushButton_update_10")
        self.pushButton_update_10.setMinimumSize(QSize(20, 0))
        self.pushButton_update_10.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_update_10, 1, 2, 1, 1)

        self.pushButton_save_11 = QPushButton(self.frame_7)
        self.pushButton_save_11.setObjectName(u"pushButton_save_11")
        self.pushButton_save_11.setMinimumSize(QSize(20, 0))
        self.pushButton_save_11.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_save_11, 1, 3, 1, 1)

        self.pushButton_update_9 = QPushButton(self.frame_7)
        self.pushButton_update_9.setObjectName(u"pushButton_update_9")
        self.pushButton_update_9.setMinimumSize(QSize(20, 0))
        self.pushButton_update_9.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_update_9, 1, 4, 1, 1)

        self.pushButton_save_8 = QPushButton(self.frame_7)
        self.pushButton_save_8.setObjectName(u"pushButton_save_8")
        self.pushButton_save_8.setMinimumSize(QSize(20, 0))
        self.pushButton_save_8.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_save_8, 1, 5, 1, 1)

        self.pushButton_update_11 = QPushButton(self.frame_7)
        self.pushButton_update_11.setObjectName(u"pushButton_update_11")
        self.pushButton_update_11.setMinimumSize(QSize(20, 0))
        self.pushButton_update_11.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_update_11, 1, 6, 1, 1)

        self.pushButton_save_9 = QPushButton(self.frame_7)
        self.pushButton_save_9.setObjectName(u"pushButton_save_9")
        self.pushButton_save_9.setMinimumSize(QSize(20, 0))
        self.pushButton_save_9.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_save_9, 1, 7, 1, 1)

        self.pushButton_update_8 = QPushButton(self.frame_7)
        self.pushButton_update_8.setObjectName(u"pushButton_update_8")
        self.pushButton_update_8.setMinimumSize(QSize(20, 0))
        self.pushButton_update_8.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_update_8, 1, 8, 1, 1)

        self.pushButton_save_10 = QPushButton(self.frame_7)
        self.pushButton_save_10.setObjectName(u"pushButton_save_10")
        self.pushButton_save_10.setMinimumSize(QSize(20, 0))
        self.pushButton_save_10.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_save_10, 1, 9, 1, 1)

        self.pushButton_update_7 = QPushButton(self.frame_7)
        self.pushButton_update_7.setObjectName(u"pushButton_update_7")
        self.pushButton_update_7.setMinimumSize(QSize(30, 0))
        self.pushButton_update_7.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_7.addWidget(self.pushButton_update_7, 1, 10, 1, 1)


        self.gridLayout_10.addWidget(self.frame_7, 3, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_add = QPushButton(self.frame_6)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_add)

        self.pushButton_save = QPushButton(self.frame_6)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_save)

        self.pushButton_update = QPushButton(self.frame_6)
        self.pushButton_update.setObjectName(u"pushButton_update")
        self.pushButton_update.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_update)

        self.pushButton_once = QPushButton(self.frame_6)
        self.pushButton_once.setObjectName(u"pushButton_once")
        self.pushButton_once.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_once)

        self.pushButton_start = QPushButton(self.frame_6)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_start)


        self.gridLayout_10.addWidget(self.frame_6, 1, 0, 1, 1)

        self.widget_9 = QWidget(self.frame_2)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 200))
        self.gridLayout_5 = QGridLayout(self.widget_9)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_3 = QLabel(self.widget_9)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color:rgb(255, 0, 0)")

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 2)

        self.label_4 = QLabel(self.widget_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.widget_9)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font1)

        self.gridLayout_5.addWidget(self.lineEdit_6, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.widget_9)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setFlat(False)

        self.gridLayout_5.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.label_5 = QLabel(self.widget_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.gridLayout_5.addWidget(self.label_5, 2, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.widget_9)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setFont(font1)

        self.gridLayout_5.addWidget(self.lineEdit_7, 2, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.widget_9)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setFlat(False)

        self.gridLayout_5.addWidget(self.pushButton_3, 2, 2, 1, 1)

        self.lineEdit_8 = QLineEdit(self.widget_9)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setFont(font1)

        self.gridLayout_5.addWidget(self.lineEdit_8, 3, 0, 1, 2)

        self.checkBox_8 = QCheckBox(self.widget_9)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setFont(font1)

        self.gridLayout_5.addWidget(self.checkBox_8, 3, 2, 1, 1)

        self.frame_9 = QFrame(self.widget_9)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_add_4 = QPushButton(self.frame_9)
        self.pushButton_add_4.setObjectName(u"pushButton_add_4")
        self.pushButton_add_4.setMaximumSize(QSize(100, 16777215))
        self.pushButton_add_4.setAutoDefault(False)
        self.pushButton_add_4.setFlat(False)

        self.horizontalLayout_3.addWidget(self.pushButton_add_4)

        self.pushButton_save_12 = QPushButton(self.frame_9)
        self.pushButton_save_12.setObjectName(u"pushButton_save_12")
        self.pushButton_save_12.setMaximumSize(QSize(100, 16777215))
        self.pushButton_save_12.setAutoDefault(False)
        self.pushButton_save_12.setFlat(False)

        self.horizontalLayout_3.addWidget(self.pushButton_save_12)

        self.pushButton_update_12 = QPushButton(self.frame_9)
        self.pushButton_update_12.setObjectName(u"pushButton_update_12")
        self.pushButton_update_12.setMaximumSize(QSize(100, 16777215))
        self.pushButton_update_12.setAutoDefault(False)
        self.pushButton_update_12.setFlat(False)

        self.horizontalLayout_3.addWidget(self.pushButton_update_12)


        self.gridLayout_5.addWidget(self.frame_9, 4, 0, 1, 3)


        self.gridLayout_10.addWidget(self.widget_9, 2, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_2, 1, 1, 2, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_20 = QGridLayout(self.tab)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.frame_13 = QFrame(self.tab)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_13)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.comboBox_plan = QComboBox(self.frame_13)
        self.comboBox_plan.setObjectName(u"comboBox_plan")
        self.comboBox_plan.setMinimumSize(QSize(200, 0))
        self.comboBox_plan.setFont(font1)

        self.gridLayout_13.addWidget(self.comboBox_plan, 0, 2, 1, 1)

        self.label_22 = QLabel(self.frame_13)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)

        self.gridLayout_13.addWidget(self.label_22, 0, 1, 1, 1)

        self.pushButton_fsave = QPushButton(self.frame_13)
        self.pushButton_fsave.setObjectName(u"pushButton_fsave")
        self.pushButton_fsave.setMinimumSize(QSize(150, 0))
        self.pushButton_fsave.setFont(font1)

        self.gridLayout_13.addWidget(self.pushButton_fsave, 0, 3, 1, 1)

        self.lineEdit_rename = QLineEdit(self.frame_13)
        self.lineEdit_rename.setObjectName(u"lineEdit_rename")

        self.gridLayout_13.addWidget(self.lineEdit_rename, 0, 6, 1, 1)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(200, 0))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.gridLayout_13.addWidget(self.frame_14, 0, 4, 1, 1)

        self.checkBox_selectall = QCheckBox(self.frame_13)
        self.checkBox_selectall.setObjectName(u"checkBox_selectall")

        self.gridLayout_13.addWidget(self.checkBox_selectall, 0, 0, 1, 1)

        self.pushButton_rename = QPushButton(self.frame_13)
        self.pushButton_rename.setObjectName(u"pushButton_rename")
        self.pushButton_rename.setFont(font1)

        self.gridLayout_13.addWidget(self.pushButton_rename, 0, 7, 1, 1)

        self.label_23 = QLabel(self.frame_13)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.gridLayout_13.addWidget(self.label_23, 0, 5, 1, 1)


        self.gridLayout_20.addWidget(self.frame_13, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.tab)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(300, 0))
        self.frame_10.setMaximumSize(QSize(300, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_10)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.textBrowser = QTextBrowser(self.frame_10)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_18.addWidget(self.textBrowser, 11, 0, 1, 1)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_12)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.checkBox_9 = QCheckBox(self.frame_12)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setFont(font1)

        self.gridLayout_15.addWidget(self.checkBox_9, 0, 0, 1, 2)

        self.checkBox_10 = QCheckBox(self.frame_12)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setFont(font1)

        self.gridLayout_15.addWidget(self.checkBox_10, 0, 2, 1, 3)

        self.checkBox_12 = QCheckBox(self.frame_12)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setFont(font1)

        self.gridLayout_15.addWidget(self.checkBox_12, 1, 0, 1, 2)

        self.checkBox_11 = QCheckBox(self.frame_12)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setFont(font1)

        self.gridLayout_15.addWidget(self.checkBox_11, 1, 2, 1, 2)

        self.checkBox_13 = QCheckBox(self.frame_12)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setFont(font1)

        self.gridLayout_15.addWidget(self.checkBox_13, 1, 4, 1, 2)

        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout_15.addWidget(self.label_10, 2, 0, 1, 2)

        self.lineEdit_13 = QLineEdit(self.frame_12)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout_15.addWidget(self.lineEdit_13, 2, 2, 1, 2)

        self.label_13 = QLabel(self.frame_12)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.gridLayout_15.addWidget(self.label_13, 2, 4, 1, 2)

        self.label_11 = QLabel(self.frame_12)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.gridLayout_15.addWidget(self.label_11, 3, 0, 1, 2)

        self.lineEdit_14 = QLineEdit(self.frame_12)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.gridLayout_15.addWidget(self.lineEdit_14, 3, 2, 1, 2)

        self.label_14 = QLabel(self.frame_12)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.gridLayout_15.addWidget(self.label_14, 3, 4, 1, 1)

        self.label_12 = QLabel(self.frame_12)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.gridLayout_15.addWidget(self.label_12, 4, 0, 1, 2)

        self.lineEdit_15 = QLineEdit(self.frame_12)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_15.addWidget(self.lineEdit_15, 4, 2, 1, 2)

        self.label_15 = QLabel(self.frame_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.gridLayout_15.addWidget(self.label_15, 4, 4, 1, 1)

        self.pushButton_18 = QPushButton(self.frame_12)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setFont(font1)
        self.pushButton_18.setStyleSheet(u"background:rgb(255,0,0)")

        self.gridLayout_15.addWidget(self.pushButton_18, 5, 0, 1, 6)

        self.label_16 = QLabel(self.frame_12)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.gridLayout_15.addWidget(self.label_16, 6, 0, 1, 1)

        self.lineEdit_16 = QLineEdit(self.frame_12)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_15.addWidget(self.lineEdit_16, 6, 1, 1, 1)

        self.label_17 = QLabel(self.frame_12)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.gridLayout_15.addWidget(self.label_17, 6, 2, 1, 1)

        self.lineEdit_17 = QLineEdit(self.frame_12)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.gridLayout_15.addWidget(self.lineEdit_17, 6, 3, 1, 2)

        self.pushButton_19 = QPushButton(self.frame_12)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setFont(font1)

        self.gridLayout_15.addWidget(self.pushButton_19, 6, 5, 1, 1)


        self.gridLayout_18.addWidget(self.frame_12, 6, 0, 1, 1)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_11)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_4 = QPushButton(self.frame_11)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font1)

        self.gridLayout_14.addWidget(self.pushButton_4, 1, 0, 1, 3)

        self.pushButton_5 = QPushButton(self.frame_11)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font1)

        self.gridLayout_14.addWidget(self.pushButton_5, 1, 3, 1, 2)

        self.lineEdit_9 = QLineEdit(self.frame_11)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_14.addWidget(self.lineEdit_9, 0, 1, 1, 5)

        self.pushButton_10 = QPushButton(self.frame_11)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font1)
        self.pushButton_10.setStyleSheet(u"background:rgb(255,0,0)")

        self.gridLayout_14.addWidget(self.pushButton_10, 2, 7, 1, 2)

        self.lineEdit_10 = QLineEdit(self.frame_11)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_14.addWidget(self.lineEdit_10, 0, 8, 1, 1)

        self.pushButton_9 = QPushButton(self.frame_11)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font1)

        self.gridLayout_14.addWidget(self.pushButton_9, 2, 0, 1, 2)

        self.pushButton_6 = QPushButton(self.frame_11)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font1)

        self.gridLayout_14.addWidget(self.pushButton_6, 1, 5, 1, 4)

        self.pushButton_7 = QPushButton(self.frame_11)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font1)

        self.gridLayout_14.addWidget(self.pushButton_7, 2, 4, 1, 3)

        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout_14.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.frame_11)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout_14.addWidget(self.label_7, 0, 6, 1, 2)

        self.pushButton_8 = QPushButton(self.frame_11)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font1)

        self.gridLayout_14.addWidget(self.pushButton_8, 2, 2, 1, 2)


        self.gridLayout_18.addWidget(self.frame_11, 4, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.frame_10)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFont(font1)
        self.gridLayout_22 = QGridLayout(self.groupBox_6)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(-1, 0, -1, 0)
        self.frame_17 = QFrame(self.groupBox_6)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_17)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(-1, 0, -1, 0)
        self.label_20 = QLabel(self.frame_17)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.gridLayout_23.addWidget(self.label_20, 0, 0, 1, 1)

        self.lineEdit_axis0 = QLineEdit(self.frame_17)
        self.lineEdit_axis0.setObjectName(u"lineEdit_axis0")
        font4 = QFont()
        font4.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font4.setPointSize(10)
        font4.setBold(False)
        self.lineEdit_axis0.setFont(font4)
        self.lineEdit_axis0.setStyleSheet(u"background:rgb(240,240,240)")
        self.lineEdit_axis0.setEchoMode(QLineEdit.Normal)
        self.lineEdit_axis0.setReadOnly(True)

        self.gridLayout_23.addWidget(self.lineEdit_axis0, 0, 1, 1, 1)

        self.label_21 = QLabel(self.frame_17)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)

        self.gridLayout_23.addWidget(self.label_21, 1, 0, 1, 1)

        self.lineEdit_axis1 = QLineEdit(self.frame_17)
        self.lineEdit_axis1.setObjectName(u"lineEdit_axis1")
        self.lineEdit_axis1.setFont(font4)
        self.lineEdit_axis1.setStyleSheet(u"background:rgb(240,240,240)")
        self.lineEdit_axis1.setEchoMode(QLineEdit.Normal)
        self.lineEdit_axis1.setReadOnly(True)

        self.gridLayout_23.addWidget(self.lineEdit_axis1, 1, 1, 1, 1)

        self.label_25 = QLabel(self.frame_17)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)

        self.gridLayout_23.addWidget(self.label_25, 2, 0, 1, 1)

        self.lineEdit_axis2 = QLineEdit(self.frame_17)
        self.lineEdit_axis2.setObjectName(u"lineEdit_axis2")
        self.lineEdit_axis2.setFont(font4)
        self.lineEdit_axis2.setStyleSheet(u"background:rgb(240,240,240)")
        self.lineEdit_axis2.setEchoMode(QLineEdit.Normal)
        self.lineEdit_axis2.setReadOnly(True)

        self.gridLayout_23.addWidget(self.lineEdit_axis2, 2, 1, 1, 1)

        self.label_26 = QLabel(self.frame_17)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)

        self.gridLayout_23.addWidget(self.label_26, 3, 0, 1, 1)

        self.lineEdit_axis3 = QLineEdit(self.frame_17)
        self.lineEdit_axis3.setObjectName(u"lineEdit_axis3")
        self.lineEdit_axis3.setFont(font4)
        self.lineEdit_axis3.setStyleSheet(u"background:rgb(240,240,240)")
        self.lineEdit_axis3.setEchoMode(QLineEdit.Normal)
        self.lineEdit_axis3.setReadOnly(True)

        self.gridLayout_23.addWidget(self.lineEdit_axis3, 3, 1, 1, 1)

        self.label_24 = QLabel(self.frame_17)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)

        self.gridLayout_23.addWidget(self.label_24, 4, 0, 1, 1)

        self.lineEdit_axis4 = QLineEdit(self.frame_17)
        self.lineEdit_axis4.setObjectName(u"lineEdit_axis4")
        self.lineEdit_axis4.setFont(font4)
        self.lineEdit_axis4.setStyleSheet(u"background:rgb(240,240,240)")
        self.lineEdit_axis4.setEchoMode(QLineEdit.Normal)
        self.lineEdit_axis4.setReadOnly(True)

        self.gridLayout_23.addWidget(self.lineEdit_axis4, 4, 1, 1, 1)


        self.gridLayout_22.addWidget(self.frame_17, 1, 0, 1, 1)

        self.frame_16 = QFrame(self.groupBox_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 0))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_16)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(-1, 0, -1, 0)
        self.checkBox_key = QCheckBox(self.frame_16)
        self.checkBox_key.setObjectName(u"checkBox_key")
        self.checkBox_key.setFont(font1)

        self.gridLayout_19.addWidget(self.checkBox_key, 0, 0, 1, 1)

        self.pushButton_ToTable = QPushButton(self.frame_16)
        self.pushButton_ToTable.setObjectName(u"pushButton_ToTable")
        self.pushButton_ToTable.setMinimumSize(QSize(0, 30))
        self.pushButton_ToTable.setFont(font1)

        self.gridLayout_19.addWidget(self.pushButton_ToTable, 0, 1, 1, 1)


        self.gridLayout_22.addWidget(self.frame_16, 0, 0, 1, 1)

        self.frame_15 = QFrame(self.groupBox_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 100))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_15)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(-1, 0, -1, 0)
        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(135, 16777215))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_18)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(-1, 0, -1, 0)
        self.label_18 = QLabel(self.frame_18)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.gridLayout_21.addWidget(self.label_18, 0, 0, 1, 1)

        self.lineEdit_CarNo = QLineEdit(self.frame_18)
        self.lineEdit_CarNo.setObjectName(u"lineEdit_CarNo")
        self.lineEdit_CarNo.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_CarNo.setAlignment(Qt.AlignCenter)

        self.gridLayout_21.addWidget(self.lineEdit_CarNo, 0, 1, 1, 1)


        self.gridLayout_24.addWidget(self.frame_18, 0, 0, 1, 1)

        self.pushButton_CardStart = QPushButton(self.frame_15)
        self.pushButton_CardStart.setObjectName(u"pushButton_CardStart")
        self.pushButton_CardStart.setMinimumSize(QSize(0, 30))
        self.pushButton_CardStart.setFont(font1)

        self.gridLayout_24.addWidget(self.pushButton_CardStart, 0, 1, 1, 1)

        self.pushButton_CardRun = QPushButton(self.frame_15)
        self.pushButton_CardRun.setObjectName(u"pushButton_CardRun")
        self.pushButton_CardRun.setMinimumSize(QSize(0, 30))
        self.pushButton_CardRun.setFont(font1)

        self.gridLayout_24.addWidget(self.pushButton_CardRun, 1, 0, 1, 1)

        self.pushButton_CardReset = QPushButton(self.frame_15)
        self.pushButton_CardReset.setObjectName(u"pushButton_CardReset")
        self.pushButton_CardReset.setMinimumSize(QSize(0, 30))
        self.pushButton_CardReset.setFont(font1)

        self.gridLayout_24.addWidget(self.pushButton_CardReset, 1, 1, 1, 1)


        self.gridLayout_22.addWidget(self.frame_15, 2, 0, 1, 1)


        self.gridLayout_18.addWidget(self.groupBox_6, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.frame_10)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font1)
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 0, -1, 5)
        self.radioButton_5 = QRadioButton(self.groupBox_4)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setFont(font1)

        self.gridLayout_6.addWidget(self.radioButton_5, 0, 1, 1, 1)

        self.radioButton_6 = QRadioButton(self.groupBox_4)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setFont(font1)

        self.gridLayout_6.addWidget(self.radioButton_6, 0, 2, 1, 1)

        self.radioButton_4 = QRadioButton(self.groupBox_4)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font1)

        self.gridLayout_6.addWidget(self.radioButton_4, 0, 0, 1, 1)


        self.gridLayout_18.addWidget(self.groupBox_4, 3, 0, 1, 1)


        self.gridLayout_20.addWidget(self.frame_10, 0, 1, 2, 1)

        self.tableWidget_Step = QTableWidget(self.tab)
        if (self.tableWidget_Step.columnCount() < 11):
            self.tableWidget_Step.setColumnCount(11)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_Step.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_Step.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_Step.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_Step.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_Step.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_Step.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_Step.setHorizontalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_Step.setHorizontalHeaderItem(7, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_Step.setHorizontalHeaderItem(8, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_Step.setHorizontalHeaderItem(9, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_Step.setHorizontalHeaderItem(10, __qtablewidgetitem20)
        self.tableWidget_Step.setObjectName(u"tableWidget_Step")
        self.tableWidget_Step.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_Step.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_Step.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_20.addWidget(self.tableWidget_Step, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.pushButton.setDefault(True)
        self.pushButton_add.setDefault(True)
        self.pushButton_save.setDefault(True)
        self.pushButton_update.setDefault(True)
        self.pushButton_once.setDefault(True)
        self.pushButton_start.setDefault(True)
        self.pushButton_2.setDefault(True)
        self.pushButton_3.setDefault(True)
        self.pushButton_add_4.setDefault(True)
        self.pushButton_save_12.setDefault(True)
        self.pushButton_update_12.setDefault(True)
        self.pushButton_fsave.setDefault(True)
        self.pushButton_rename.setDefault(True)
        self.pushButton_19.setDefault(True)
        self.pushButton_4.setDefault(True)
        self.pushButton_5.setDefault(True)
        self.pushButton_9.setDefault(True)
        self.pushButton_6.setDefault(True)
        self.pushButton_7.setDefault(True)
        self.pushButton_8.setDefault(True)
        self.pushButton_ToTable.setDefault(True)
        self.pushButton_CardStart.setDefault(True)
        self.pushButton_CardRun.setDefault(True)
        self.pushButton_CardReset.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e2d\u63a7", None))
        ___qtablewidgetitem = self.tableWidget_Results.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u671f\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget_Results.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u8dd1\u65f6\u95f4", None));
        ___qtablewidgetitem2 = self.tableWidget_Results.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u5012\u6570", None));
        ___qtablewidgetitem3 = self.tableWidget_Results.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001", None));
        ___qtablewidgetitem4 = self.tableWidget_Results.horizontalHeaderItem(5)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u8d5b\u679c", None));
        ___qtablewidgetitem5 = self.tableWidget_Results.horizontalHeaderItem(6)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u8d5b\u679c", None));
        ___qtablewidgetitem6 = self.tableWidget_Results.horizontalHeaderItem(7)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247", None));
        ___qtablewidgetitem7 = self.tableWidget_Results.horizontalHeaderItem(8)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u50cf", None));
        ___qtablewidgetitem8 = self.tableWidget_Results.horizontalHeaderItem(9)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u590d\u76d8", None));
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u76d8\u53e3\u72b6\u6001", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u76d8", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5c01\u76d8", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u62df", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u9ed1\u5c4f", None))
        self.groupBox_status.setTitle(QCoreApplication.translate("MainWindow", u"\u72b6\u60011", None))
        self.status_live.setText(QCoreApplication.translate("MainWindow", u"\u76f4\u64ad\u72b6\u6001", None))
        self.status_road.setText(QCoreApplication.translate("MainWindow", u"\u8d5b\u9053\u72b6\u6001", None))
        self.status_lenses.setText(QCoreApplication.translate("MainWindow", u"\u955c\u5934\u72b6\u6001", None))
        self.status_track.setText(QCoreApplication.translate("MainWindow", u"\u8f68\u9053\u72b6\u6001", None))
        self.groupBox_status_2.setTitle(QCoreApplication.translate("MainWindow", u"\u72b6\u60012", None))
        self.status_server1.setText(QCoreApplication.translate("MainWindow", u"\u6392\u540d\u670d\u52a1\u5668", None))
        self.status_server2.setText(QCoreApplication.translate("MainWindow", u"\u6392\u540d\u670d\u52a1\u56682", None))
        self.status_sportsCards.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u52a8\u5361", None))
        self.status_obs.setText(QCoreApplication.translate("MainWindow", u"OBS\u72b6\u6001", None))
        self.status_mainlenses.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u955c\u5934", None))
        self.status_Recognition.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u8bc6\u522b1", None))
        self.status_Extension.setText(QCoreApplication.translate("MainWindow", u"\u5206\u673a1", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u529f\u80fd", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u8df3\u8fc7\u8d77\u70b9\u8bc6\u522b", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5c40\u7ed3\u675f\u540e\u81ea\u52a8\u9ed1\u5c4f", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u8df3\u8fc7\u8d77\u4e8c\u6b21\u6392\u540d", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5c40\u7ed3\u675f\u540e\u81ea\u52a8\u5c01\u76d8", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u5f39\u5c04", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"\u5173\u8b66\u62a5", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u9501\u5b9a\u671f\u53f7", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7c92", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8d77\u70b9\u73e0\u5b50\u6570\u91cf\uff1a", None))
        self.pushButton_add_3.setText(QCoreApplication.translate("MainWindow", u"\u8f68\u9053\u505c\u6b62", None))
        self.pushButton_start_2.setText(QCoreApplication.translate("MainWindow", u"\u6536\u5de5", None))
        self.pushButton_add_2.setText(QCoreApplication.translate("MainWindow", u"\u5361\u73e0", None))
        self.pushButton_save_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_update_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_save_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_update_3.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_save_4.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_update_5.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_save_5.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_update_4.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_save_6.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_update_6.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton_once_2.setText(QCoreApplication.translate("MainWindow", u"\u98de\u73e0", None))
        self.pushButton_save_7.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_update_10.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_save_11.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_update_9.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_save_8.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_update_11.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_save_9.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_update_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_save_10.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_update_7.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"\u51c6\u5907", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.pushButton_update.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u5173", None))
        self.pushButton_once.setText(QCoreApplication.translate("MainWindow", u"\u6536\u73e0", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8d5b\u679c\u786e\u8ba4 \u8bc6\u522b\u72b6\u6001", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u6444\u50cf\u673a\uff1a  ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u9009", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u540e\u5907\u6444\u50cf\u673a\uff1a", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u9009", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8", None))
        self.pushButton_add_4.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4\u8d5b\u679c", None))
        self.pushButton_save_12.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88\u5f53\u5c40", None))
        self.pushButton_update_12.setText(QCoreApplication.translate("MainWindow", u"\u7ec8\u70b9\u8bc6\u522b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u76f4\u64ad\u5927\u5385", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u65b9\u6848\uff1a", None))
        self.pushButton_fsave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u65b9\u6848", None))
        self.checkBox_selectall.setText(QCoreApplication.translate("MainWindow", u"\u5168\u9009", None))
        self.pushButton_rename.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u547d\u540d\u65b9\u6848", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u65b9\u6848\u540d\u79f0\uff1a", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"\u80cc\u666f\u5f55\u56fe", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u901f\u95f8\u95e8", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u5f55\u8bef\u5224", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"\u8ffd\u8e2a", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u56fe", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u5c01\u76d8\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u79d2\uff08\u6700\u540e\u8fdb\u7ec8\u70b9\u8d77\u7b97\uff09", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u6536\u73e0\u5f39\u5c04\uff1a", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u79d2", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u8f68\u9053\u62a5\u8b66\uff1a", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u79d2", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"\u8f68\u9053\u505c\u6b62", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u8f74\uff1a", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u7edf\u4e00\uff1a", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u5f00", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u5173", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u673a1", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u753b\u4e2d\u753b", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u673a3", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u56fe\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6570\u91cf\uff1a", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u673a2", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e\u8ddf\u8e2a", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u8f741\uff1a", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u8f742\uff1a", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u8f743\uff1a", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u8f744\uff1a", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u8f745\uff1a", None))
        self.checkBox_key.setText(QCoreApplication.translate("MainWindow", u"\u952e\u76d8\u5b9a\u4f4d", None))
        self.pushButton_ToTable.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807\u5165\u8868", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u52a8\u5361\u53f7\uff1a", None))
        self.pushButton_CardStart.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u8fd0\u52a8\u5361", None))
        self.pushButton_CardRun.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u52a8\u5f00\u542f", None))
        self.pushButton_CardReset.setText(QCoreApplication.translate("MainWindow", u"\u590d\u4f4d", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5708\u6570\u9009\u62e9", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"\u5708\u65702", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"\u5708\u65703", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u5708\u65701", None))
        ___qtablewidgetitem9 = self.tableWidget_Step.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u5708\u6570", None));
        ___qtablewidgetitem10 = self.tableWidget_Step.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u5de6\u53f3", None));
        ___qtablewidgetitem11 = self.tableWidget_Step.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u524d\u540e", None));
        ___qtablewidgetitem12 = self.tableWidget_Step.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e0b", None));
        ___qtablewidgetitem13 = self.tableWidget_Step.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u5934\u65cb\u8f6c", None));
        ___qtablewidgetitem14 = self.tableWidget_Step.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u5934\u4e0a\u4e0b", None));
        ___qtablewidgetitem15 = self.tableWidget_Step.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6", None));
        ___qtablewidgetitem16 = self.tableWidget_Step.horizontalHeaderItem(8)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u901f", None));
        ___qtablewidgetitem17 = self.tableWidget_Step.horizontalHeaderItem(9)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u51cf\u901f", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u8fd0\u52a8\u53c2\u6570", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u8bc6\u522b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u955c\u5934\u8bbe\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u5206\u673a\u7ba1\u7406", None))
    # retranslateUi

