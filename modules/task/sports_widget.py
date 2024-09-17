from PySide6.QtCore import QThread, Signal


class SportsThread(QThread):
    update_signal = Signal(int, int,str)
    def __init__(self,row:int,col:int,text:str):
        super().__init__()
        self.row = row
        self.col = col
        self.text = text
    # 定义信号，用于更新多个控件


    def run(self):
        self.update_signal.emit(self.row,self.col,self.text)