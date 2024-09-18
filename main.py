import json
import re
from PySide6.QtCore import QObject,Qt
from PySide6.QtWidgets import QMainWindow, QMenu, QComboBox, QCheckBox, QApplication, QWidget, QHBoxLayout, \
    QTableWidgetItem, QInputDialog, QDialog, QMessageBox
from Ui_MainCtl_Ui import Ui_MainWindow
from modules.controls.message_box import  MessageBox
from modules.controls.plan_dialog import PlanDialog
from modules.db.plan_db import PlanDb
from modules.db.track_db import TrackDb
from modules.tcp.tcp_server import TcpServer
from modules.utils.assignment import ListUtil

#  初始化数据库
def initDB():
    PlanDb.createDB()
    TrackDb.createDB()

class MasterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tcpServer = TcpServer()
        self.menu = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUi()
        self.bind()

    def initUi(self):
        self.planboBoxInit()
        self.tableInit()


    def bind(self):
        # 保存方案
        self.ui.pushButton_fsave.clicked.connect(self.fsaveAction)
        # 全选
        self.ui.checkBox_selectall.stateChanged.connect(self.checkBoxAllAction)
        # 绑定gas,obs状态监听
        self.tcpServer.gas_connection_signal.connect(self.gasStatus)
        self.tcpServer.obs_connection_signal.connect(self.obsStatus)
        self.ui.comboBox_plan.currentTextChanged.connect(self.planChange)
        self.ui.tableWidget_Step.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.tableWidget_Step.customContextMenuRequested.connect(self.onCustomRequested)
        self.ui.tableWidget_Step.cellChanged.connect(self.handle_item_changed)

    def gasStatus(self,flag:bool):
        if flag:
            self.ui.status_sportsCards.setStyleSheet("background:rgb(0, 255, 0)")
        else:
            self.ui.status_sportsCards.setStyleSheet("background:rgb(255, 0, 0)")
    def obsStatus(self,flag:bool):
        if flag:
            self.ui.status_obs.setStyleSheet("background:rgb(0, 255, 0)")
        else:
            self.ui.status_obs.setStyleSheet("background:rgb(255, 0, 0)")

    def planChange(self,text:str):
        global sport_tables
        planList: list = PlanDb.findByName(text)
        plan_id = 0
        if planList:
            plan_id =  planList[0][0]
        if plan_id!=0:
            trackList = TrackDb.findByPlan(plan_id)
            if trackList:
                sport_tables = ListUtil.assign(trackList)
                self.tableInit()

    #  初始化方案，并初始化列表数据
    def planboBoxInit(self):
        global sport_tables
        planList:list = PlanDb.findAll()
        plan = None
        if planList:
            plan = planList[0]
            for item in planList:
                if item[2]==1:
                    plan = item
                self.ui.comboBox_plan.addItem(item[1])
            self.ui.comboBox_plan.setCurrentText(plan[1])
        if plan:
            trackList =  TrackDb.findByPlan(plan[0])
            if trackList:
                sport_tables =  ListUtil.assign(trackList)
            else:
                sport_tables =  ListUtil.initAssign()
        else:
            sport_tables = ListUtil.initAssign()

    #  全选项
    def checkBoxAllAction(self,state):
        flag = False
        if state==2:
            flag = True
        for row in range(self.ui.tableWidget_Step.rowCount()):
            checkbox = self.ui.tableWidget_Step.cellWidget(row, 0)  # Get the checkbox in the first column
            checkbox.setChecked(flag)

    # 保存方案的信息
    def fsaveAction(self):
        global sport_tables
        planDialog =  PlanDialog()
        if planDialog.exec() == QDialog.DialogCode.Accepted:
            user_input = planDialog.get_input()
            if user_input!="":
                # 添加方案
                switch_status = 1 if planDialog.is_switch_on() else 0
                if switch_status==1:
                    PlanDb.updateAllDefault()
                plan_id = PlanDb.insertDb(user_input,switch_status)
                # 添加数据
                for index, item in enumerate(sport_tables):
                    model:dict = {"num":index,"plan_id":plan_id,"circle":item[1],"move":item[2],"axis1":item[3],"axis2":item[4],
                             "axis3":item[5], "axis4":item[6],"axis5":item[7], "vel":item[8],"start":item[9],"brake":item[10],
                             "zoom_in":item[11],"zoom_out":item[12],"pros_cons":item[13],"delay":"","take_time":"","organ":item[14]}
                    TrackDb.insertDb(model)
                MessageBox("添加成功!", "").exec()
                planList: list = PlanDb.findAll()
                if planList and len(planList):
                    for item in planList:
                        self.ui.comboBox_plan.addItem(item[1], item[0])
            else:
                MessageBox("警告!","请输入方案名称,未能保存方案").exec()



    # 初始化运动参数tableWidget
    def tableInit(self):
        global sport_tables
        for index,item in enumerate(sport_tables):
            self.ui.tableWidget_Step.setRowCount(index + 1)
            if index==0 or index==1:
                self.ui.tableWidget_Step.setColumnWidth(index, 40)
            if index == 2:
                self.ui.tableWidget_Step.setColumnWidth(index, 60)
            if index >= 8:
                self.ui.tableWidget_Step.setColumnWidth(index, 60)
            cb = QCheckBox()
            cb.setStyleSheet('QCheckBox{margin:12px };')
            self.ui.tableWidget_Step.setCellWidget(index, 0, cb)
            comboBox = QComboBox()
            comboBox.addItems(["直线", "圆弧"])
            self.ui.tableWidget_Step.setCellWidget(index, 2, comboBox)
            for key, value in item.items():
                val = QTableWidgetItem(str(value))
                self.ui.tableWidget_Step.setItem(index, key, val)


    # 表格更新的同步表数据
    def handle_item_changed(self,row,column):
        global sport_tables
        item = self.ui.tableWidget_Step.item(row, column)
        if item:
            if re.match(r'^\d+(\.\d+)?$', item.text()) is not None:
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                if item:
                    sport_tables[row][column] = item.text()
            else:
                item.setText("")


    # 监听右键点击事件
    def onCustomRequested(self,pos):
        global_pos = self.ui.tableWidget_Step.mapToGlobal(pos)
        row = self.ui.tableWidget_Step.rowAt(pos.y())
        if row >= 0:
            menu = QMenu()
            add = menu.addAction("新增一行")
            add.triggered.connect(self.addActionTriggered)
            insert = menu.addAction("插入一行")
            insert.triggered.connect(lambda:self.insertActionTriggered(row))
            clear = menu.addAction("清空")
            clear.triggered.connect(self.clearActionTriggered)
            edit = menu.addAction("修改数据")
            edit.triggered.connect(self.editActionTriggered)
            run = menu.addAction("运行")
            run.triggered.connect(self.runActionTriggered)
            menu.exec(global_pos)
    # 新增
    def addActionTriggered(self):
        self.ui.tableWidget_Step.insertRow(1)
        comboBox = QComboBox()
        comboBox.addItems([ "直线", "圆弧"])
        checkBox = QCheckBox()
        checkBox.setStyleSheet('QCheckBox{margin:12px };')
        self.ui.tableWidget_Step.setCellWidget(1, 0, checkBox)
        self.ui.tableWidget_Step.setCellWidget(1, 2, comboBox)
    # 插入
    def insertActionTriggered(self,row):
        self.ui.tableWidget_Step.insertRow(row)
        comboBox = QComboBox()
        comboBox.addItems(["直线", "圆弧"])
        checkBox = QCheckBox()
        checkBox.setStyleSheet('QCheckBox{margin:12px };')
        self.ui.tableWidget_Step.setCellWidget(row, 0, checkBox)
        self.ui.tableWidget_Step.setCellWidget(row, 2, comboBox)
    # 清空
    def clearActionTriggered(self):
        for row in range(self.ui.tableWidget_Step.rowCount()):
            for column in range(self.ui.tableWidget_Step.columnCount()):
                self.ui.tableWidget_Step.setItem(row, column, None)
    # 修改数据
    def editActionTriggered(self):
        pass
    # 运行
    def runActionTriggered(self):
        global sport_tables
        # 选中行的数据
        row_list = []
        # 循环行
        for row in range(self.ui.tableWidget_Step.rowCount()):
            checkbox = self.ui.tableWidget_Step.cellWidget(row, 0)  # Get the checkbox in the first column
            if checkbox.isChecked():
                dict_map = sport_tables[row]
                row_list.append(dict_map)
        if len(row_list)>0:
            # 发送socket
            for item in row_list:
                if item[3] and item[4] and item[5] and item[6] and item[7] and item[8] and item[9] and item[10]:
                    obj = json.dumps({
                        "type": "gas_crd",
                        "message": "%s|%s|%s|%s|%s|%s|%s|%s" % (item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10])
                    })
                    self.tcpServer.broadcast_message(obj)
                if item[12] !="":
                    self.tcpServer.broadcast_message(json.dumps({
                        "type": "gas_io_test",
                        "message": "%s|%s" % ("1", item[12])}))


if __name__ == '__main__':
    sport_tables = []
    initDB()
    app = QApplication([])
    window = MasterWindow()
    window.show()
    app.exec()


