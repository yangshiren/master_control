from PySide6.QtCore import QObject,Qt
from PySide6.QtWidgets import QMainWindow, QMenu, QComboBox, QCheckBox, QApplication
from Ui_MainCtl_Ui import Ui_MainWindow


class MasterWindow(QMainWindow,QObject):
    def __init__(self):
        super().__init__()
        self.menu = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUi()

    def initUi(self):
        self.tableInit()

    # tableWidget 添加右键按钮
    def tableInit(self):
        self.ui.tableWidget_Step.setRowCount(20)
        for row in range(self.ui.tableWidget_Step.rowCount()):
            comboBox = QComboBox()
            comboBox.addItems(["直线", "圆弧"])
            checkBox = QCheckBox()
            self.ui.tableWidget_Step.setCellWidget(row, 0, checkBox)
            self.ui.tableWidget_Step.setCellWidget(row, 2, comboBox)
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
            menu.exec_(global_pos)
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
        pass

if __name__ == '__main__':
    app = QApplication([])
    window = MasterWindow()
    window.show()
    app.exec()


