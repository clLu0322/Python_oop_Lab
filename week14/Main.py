from WorkWidgets.MainWidget import MainWidget
from PyQt6.QtWidgets import QApplication
from SocketClient import SocketClient
from ServiceController import ServiceController
import sys

HOST = "127.0.0.1"
PORT = 20001

app = QApplication([])
socket = SocketClient(HOST, PORT)
ServiceController.socket_client = socket
main_window = MainWidget()

main_window.setFixedSize(800, 500)
main_window.show()
# main_window.showFullScreen()

sys.exit(app.exec())
