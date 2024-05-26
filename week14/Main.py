from WorkWidgets.MainWidget import MainWidget
from PyQt6.QtWidgets import QApplication
from SocketClient import SocketClient
import sys

HOST = "127.0.0.1"
PORT = 20001

app = QApplication([])
socket = SocketClient(HOST, PORT)
main_window = MainWidget(socket)

main_window.setFixedSize(800, 500)
main_window.show()
# main_window.showFullScreen()

sys.exit(app.exec())
