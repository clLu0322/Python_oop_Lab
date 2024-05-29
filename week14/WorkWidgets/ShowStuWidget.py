from PyQt6 import QtWidgets
from WorkWidgets.WidgetComponents import LabelComponent, TextEditComponent, ScrollAreaComponent
from ServiceController import ExecuteCommand
import json


class ShowStuWidget(QtWidgets.QWidget):
    def __init__(self, socket):
        super().__init__()
        self.socket = socket
        self.setObjectName("show_stu_widget")
        layout = QtWidgets.QVBoxLayout()

        header_label = LabelComponent(20, "Show Student")
        self.label = LabelComponent(14, " ")
        self.scrollarea = ScrollAreaComponent(self.label)

        layout.addWidget(header_label, stretch=1)
        layout.addWidget(self.scrollarea, stretch=8)

        self.setLayout(layout)
    
    def show_action(self):
        self.send_command = ExecuteCommand(self.socket, "show")
        self.send_command.start()
        self.send_command.return_sig.connect(self.print_data)

    def print_data(self, result):
        result = json.loads(result)
        student_dict = result['message']['parameters']
        
        self.label.clear()
        text = "\n====== student list ======\n"
        for name, dict in student_dict.items():
            text += f"Name:{name}\n"
            for subject, score in dict["scores"].items():
                text += f"    subject: {subject}, score:{score}\n"
            text += "\n"
        text += "======================"
        self.label.setText(text)
        # self.textedit.setReadOnly(True)
    
    def load(self):
        self.show_action()
        print("\nShow All\n")
