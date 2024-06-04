from PyQt6 import QtWidgets
from WorkWidgets.WidgetComponents import LabelComponent, ScrollAreaComponent
from ServiceController import ExecuteCommand
import json


class ShowStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("show_stu_widget")
        layout = QtWidgets.QVBoxLayout()
        self.label = LabelComponent(14, "", "balck")
        self.label.set_font_weight(1000)
        self.label.set_vertical_alignment("top")
        self.scrollarea = ScrollAreaComponent(self.label)

        layout.addWidget(self.scrollarea, stretch=1)

        self.setLayout(layout)
    
    def show_action(self):
        self.send_command = ExecuteCommand("show")
        self.send_command.start()
        self.send_command.return_sig.connect(self.print_data)

    def print_data(self, result):
        result = json.loads(result)
        student_dict = result['parameters']
        
        self.label.clear()
        text = "====== student list ======\n"
        for name, dict in student_dict.items():
            text += f"Name:{name}\n"
            for subject, score in dict["scores"].items():
                text += f"    subject: {subject}, score:{score}\n"
            text += "\n"
        text += "======================"
        self.label.setText(text)
    
    def load(self):
        self.show_action()
