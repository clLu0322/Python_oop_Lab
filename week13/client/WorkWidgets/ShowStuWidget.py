from PyQt6 import QtWidgets
from WorkWidgets.WidgetComponents import LabelComponent, TextEditComponent
from ServiceController import ExecuteCommand
import json


class ShowStuWidget(QtWidgets.QWidget):
    def __init__(self, socket):
        super().__init__()
        self.socket = socket
        self.setObjectName("show_stu_widget")
        layout = QtWidgets.QVBoxLayout()

        header_label = LabelComponent(20, "Show Student")
        self.textedit = TextEditComponent()

        self.show_action()

        layout.addWidget(header_label, stretch=1)
        layout.addWidget(self.textedit, stretch=8)
        self.setLayout(layout)
    
    def show_action(self):
        self.send_command = ExecuteCommand(self.socket, "show")
        self.send_command.start()
        self.send_command.return_sig.connect(self.print_data)

    def print_data(self, result):
        result = json.loads(result)
        student_dict = result['message']['parameters']
        
        self.textedit.clear()
        text = "\n====== student list ======\n"
        for name, dict in student_dict.items():
            text += f"Name:{name}\n"
            for subject, score in dict["scores"].items():
                text += f"    subject: {subject}, score:{score}\n"
            text += "\n"
        text += "======================"
        self.textedit.setText(text)
        self.textedit.setReadOnly(True)