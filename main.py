import json

from PySide6.QtCore import QObject,Qt
from PySide6.QtWidgets import QMainWindow, QMenu, QComboBox, QCheckBox, QApplication, QWidget, QHBoxLayout, \
    QTableWidgetItem
from Ui_MainCtl_Ui import Ui_MainWindow
from modules.db.plan_db import PlanDb
from modules.db.track_db import TrackDb
from modules.tcp.tcp_server import TcpServer


class CenteredWidget(QWidget):
    def __init__(self, widget, parent=None):
        super().__init__(parent)
        # Create a layout and add the widget to it
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the widget
        layout.addWidget(widget)
        self.setLayout(layout)

#  初始化数据库
def initDB():
    PlanDb.createDB()
    TrackDb.createDB()

class MasterWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.worker_thread = None
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
        self.ui.pushButton_fsave.clicked.connect(self.fsaveAction)
        self.ui.checkBox_selectall.stateChanged.connect(self.checkBoxAllAction)

    #  初始化方案，并初始化列表数据
    def planboBoxInit(self):
        global sport_tables
        planList:list = PlanDb.findAll()
        if planList and len(planList):
            plan_id = planList[0][0]
            for item in planList:
                if item[2]==1:
                    plan_id = item[2]
                self.ui.comboBox_plan.addItem(item[1],item[0])
            trackList =  TrackDb.findByPlan(plan_id)
            for temp in trackList:
                sport_tables.append({temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],temp[10]})
        else:
            for _ in range(20):
                sport_tables.append({1:"",2:"直线",3:"",4:"",5:"",6:"",7:"",8:"",9:"",10:"",11:"",12:""})


    # # tcp server 发送消息
    # def send_message(self,message):
    #     self.tcpServer.broadcast_message(message)
    #  全选项
    def checkBoxAllAction(self,state):
        flag = False
        if state==2:
            flag = True
        for row in range(self.ui.tableWidget_Step.rowCount()):
            checkbox = self.ui.tableWidget_Step.cellWidget(row, 0)  # Get the checkbox in the first column
            checkbox.setChecked(flag)


    # 保存表格的信息
    def fsaveAction(self):
        print("------------")

    # tableWidget 添加右键按钮
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
            for key, value in item.items():
                val = QTableWidgetItem(str(value))
                val.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.ui.tableWidget_Step.setItem(index, key, val)
        self.ui.tableWidget_Step.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.tableWidget_Step.customContextMenuRequested.connect(self.onCustomRequested)
        self.ui.tableWidget_Step.cellChanged.connect(self.handle_item_changed)

    # 表格更新的同步表数据
    def handle_item_changed(self,row,column):
        global sport_tables
        item = self.ui.tableWidget_Step.item(row, column)
        sport_tables[row][column] = item.text()

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
        self.ui.tableWidget_Step.setCellWidget(1, 0, checkBox)
        self.ui.tableWidget_Step.setCellWidget(1, 2, comboBox)
    # 插入
    def insertActionTriggered(self,row):
        self.ui.tableWidget_Step.insertRow(row)
        comboBox = QComboBox()
        comboBox.addItems(["直线", "圆弧"])
        checkBox = QCheckBox()
        self.ui.tableWidget_Step.setCellWidget(row, 0, checkBox)
        self.ui.tableWidget_Step.setCellWidget(row, 2, comboBox)
    # 清空
    def clearActionTriggered(self):
        for row in range(self.ui.tableWidget_Step.rowCount()):
            for column in range(self.ui.tableWidget_Step.columnCount()):
                self.ui.tableWidget_Step.setItem(row, column, None)
    # 编辑
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
                print(item[3] , item[4] , item[5] , item[6] , item[7] , item[8] , item[9] , item[10])
                if item[3] and item[4] and item[5] and item[6] and item[7] and item[8] and item[9] and item[10]:
                    obj = json.dumps({
                        "type": "GAS_CRD",
                        "message": "%s|%s|%s|%s|%s|%s|%s|%s" % (
                        item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10])
                    })
                    self.tcpServer.broadcast_message(obj)
                if item[12] !="":
                    self.tcpServer.broadcast_message(json.dumps({
                        "type": "GAS_IO",
                        "message": "%s|%s" % ("1", item[12])
                    }))


if __name__ == '__main__':
    sport_tables = []
    initDB()
    app = QApplication([])
    window = MasterWindow()
    window.show()
    app.exec()


