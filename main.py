from PySide6.QtCore import QObject,Qt
from PySide6.QtWidgets import QMainWindow, QMenu, QComboBox, QCheckBox, QApplication, QWidget, QHBoxLayout
from Ui_MainCtl_Ui import Ui_MainWindow
from modules.db.track_data import TrackData
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

class MasterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tcpServer = None
        TrackData.createDB()
        self.menu = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUi()
        self.bind()

    def initUi(self):
        self.tableInit()

    def bind(self):
        self.ui.pushButton_fsave.clicked.connect(self.fsaveAction)
        self.ui.checkBox_selectall.stateChanged.connect(self.checkBoxAllAction)
        self.tcpServer = TcpServer()

    # # tcp server 发送消息
    # def send_message(self,message):
    #     self.tcpServer.broadcast_message(message)
    def checkBoxAllAction(self,state):
        flag = False
        if state==2:
            flag = True
        for row in range(self.ui.tableWidget_Step.rowCount()):
            checkbox = self.ui.tableWidget_Step.cellWidget(row, 0)  # Get the checkbox in the first column
            if checkbox:
                checkbox.setChecked(flag)


    # 保存表格的信息
    def fsaveAction(self):
        print("------------")

    # tableWidget 添加右键按钮
    def tableInit(self):
        self.ui.tableWidget_Step.setRowCount(20)
        for row in range(self.ui.tableWidget_Step.rowCount()):
            comboBox = QComboBox()
            comboBox.addItems(["直线", "圆弧"])
            checkBox = QCheckBox()
            checkbox_widget = CenteredWidget(checkBox)
            combobox_widget = CenteredWidget(comboBox)
            self.ui.tableWidget_Step.setCellWidget(row, 0, checkbox_widget)
            self.ui.tableWidget_Step.setCellWidget(row, 2, combobox_widget)
        self.ui.tableWidget_Step.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.tableWidget_Step.customContextMenuRequested.connect(self.onCustomRequested)

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
        # 选中行的数据
        row_list = []
        # 循环行
        for row in range(self.ui.tableWidget_Step.rowCount()):
            checkbox = self.ui.tableWidget_Step.cellWidget(row, 0)
            if checkbox.isChecked():
                row_data={}
                for col in range(self.ui.tableWidget_Step.columnCount()):
                    item = self.ui.tableWidget_Step.item(row, col)
                    temp = None
                    if col == 2:
                        temp = self.ui.tableWidget_Step.cellWidget(row, col).currentText()
                    else:
                        temp =  item.text() if item else None
                    row_data[col + 1] = temp
                row_list.append(row_data)
        # 发送socket
        for item in row_list:
            self.tcpServer.broadcast_message("")

if __name__ == '__main__':
    app = QApplication([])
    window = MasterWindow()
    window.show()
    app.exec()


