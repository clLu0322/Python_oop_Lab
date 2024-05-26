from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal
import json


class ExecuteCommand(QtCore.QThread):
    return_sig = pyqtSignal(str)

    def __init__(self, socket, command, parameters={}):
        super().__init__()
        self.socket = socket
        self.command = command
        self.parameters = parameters
        
    def run(self):
        result_dict = dict()
        self.socket.send_command(self.command, self.parameters)
        result_dict['message'] = self.socket.wait_response()
        self.return_sig.emit(json.dumps(result_dict))