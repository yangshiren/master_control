from PySide6.QtCore import QObject, Slot
from PySide6.QtNetwork import QTcpServer, QTcpSocket, QHostAddress

'''
    以\n分隔符 拆分消息， 用读取行，不处理粘包
'''
class TcpServer(QObject):
    def __init__(self):
        super().__init__()
        # Initialize QTcpServer
        self.clients:list[QTcpSocket] = []
        self.server = QTcpServer(self)
        self.server.newConnection.connect(self.on_new_connection)

        # Start listening on port 12345
        if not self.server.listen(address= QHostAddress("192.168.0.217"), port=18888):
            print(f"Server failed to start: {self.server.errorString()}")
        else:
            print("Server started successfully on port 18888")

    @Slot()
    def on_new_connection(self):
        # Get the new connection
        socket = self.server.nextPendingConnection()
        print(f"New connection from {socket.peerAddress().toString()}:{socket.peerPort()}")
        self.clients.append(socket)
        # Connect the readyRead signal to the slot
        socket.readyRead.connect(lambda: self.read_data(socket))
        socket.disconnected.connect(lambda: self.remove_client(socket))

    @Slot()
    def read_data(self, socket: QTcpSocket):
        while socket.bytesAvailable():
            data = socket.readLine()
            if data:
                print(f"Received data: {data.decode()}")

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