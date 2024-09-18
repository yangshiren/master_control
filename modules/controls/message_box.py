from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMessageBox


class MessageBox(QMessageBox):
    def __init__(self, title, message, timeout=2000):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(message)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)

        # 创建定时器，设置自动关闭
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.close)
        self.timer.start(timeout)