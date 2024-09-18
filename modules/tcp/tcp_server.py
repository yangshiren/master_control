import json

from PySide6.QtCore import QObject, Slot,Signal
from PySide6.QtNetwork import QTcpServer, QTcpSocket, QHostAddress, QAbstractSocket

from modules.utils.log_util import succeed, fail

'''
    以\n分隔符 拆分消息， 用读取行，不处理粘包
'''
class TcpServer(QObject):
    gas_connection_signal = Signal(bool)
    obs_connection_signal = Signal(bool)
    log_signal   = Signal(str)
    def __init__(self):
        super().__init__()
        # Initialize QTcpServer
        self.clients:list[QTcpSocket] = []
        self.server = QTcpServer(self)
        self.server.newConnection.connect(self.on_new_connection)
        self.server.acceptError.connect(self.on_accept_error)
        # Start listening on port 12345
        if not self.server.listen(address= QHostAddress("192.168.0.217"), port=18888):
            print(f"Server failed to start: {self.server.errorString()}")
        else:
            print("Server started successfully on port 18888")

    @Slot()
    def on_new_connection(self):
        socket = self.server.nextPendingConnection()
        self.clients.append(socket)
        socket.readyRead.connect(lambda: self.read_data(socket))
        socket.disconnected.connect(lambda: self.remove_client(socket))

    @Slot()
    def on_accept_error(self,err:QAbstractSocket.SocketError):
        self.log_signal.emit(fail("【客户端】连入失败,[%s]--[%s]"%(err.name,err.value)))

    @Slot()
    def read_data(self, socket: QTcpSocket):
        while socket.bytesAvailable():
            data = socket.readLine()
            if data:
                # 解析数据
                msg = json.loads(data.data().decode("utf-8"))
                typeMsg = msg["type"]
                if typeMsg=="gas_connection_success":
                    self.gas_connection_signal.emit(True)
                    self.log_signal.emit(succeed(msg["message"]))
                elif typeMsg=="obs_connection_success":
                    self.obs_connection_signal.emit(True)
                    self.log_signal.emit(succeed(msg["message"]))

    @Slot()
    def remove_client(self, socket: QTcpSocket):
        self.clients.remove(socket)
        print(f"remove_client")
        socket.deleteLater()

    def broadcast_message(self, message: str):
        """Send a message to all connected clients."""
        message+="\n"
        for client in self.clients:
            if client.state() == QTcpSocket.SocketState.ConnectedState:
                client.write(message.encode("utf-8"))
                client.flush()