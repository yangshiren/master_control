from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QRadioButton, QPushButton, QLabel


class PlanDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("保存方案")
        self.setGeometry(400,400, 300,150)
        self.layout = QVBoxLayout(self)

        # 添加输入框
        self.input_label = QLabel("", self)
        self.input_line_edit = QLineEdit(self)
        self.input_line_edit.setPlaceholderText("请输入方案名称")
        self.layout.addWidget(self.input_line_edit)

        # 添加开关（使用 QLabel 和 QPushButton 模拟开关）
        self.switch_button = QPushButton("是否默认", self)
        self.switch_button.setCheckable(True)
        self.switch_button.toggled.connect(self.toggle_switch)

        self.layout.addWidget(self.switch_button)

        # 添加确认按钮
        self.ok_button = QPushButton("确定", self)
        self.ok_button.clicked.connect(self.accept)

        self.layout.addWidget(self.ok_button)

        # 初始化开关状态
        self.switch_on = False

    def toggle_switch(self, checked):
        self.switch_on = checked

    def get_input(self):
        return self.input_line_edit.text()

    def is_switch_on(self):
        return self.switch_on