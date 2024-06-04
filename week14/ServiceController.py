from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal
import json

class ServiceController:
    socket_client = None

    def command_sender(self, command, data):
        self.socket_client.send_command(command, data)
        result = self.socket_client.wait_response()
        return result

class ExecuteCommand(QtCore.QThread):
    return_sig = pyqtSignal(str)

    def __init__(self, command, parameters={}):
        super().__init__()
        self.command = command
        self.parameters = parameters
        
    def run(self):
        result_dict = dict()
        result_dict = ServiceController().command_sender(self.command, self.parameters)
        self.return_sig.emit(json.dumps(result_dict))