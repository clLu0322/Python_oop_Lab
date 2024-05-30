from PyQt6 import QtWidgets
import json
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent, TextEditComponent, MessageBoxComponent
from ServiceController import ExecuteCommand

class DelStuWidget(QtWidgets.QWidget):
    def __init__(self, socket):
         super().__init__()
         self.socket = socket
         self.setObjectName("del_stu_widget")
         self.layout = QtWidgets.QGridLayout()

         self.header_label = LabelComponent(20, "Del Student")
         self.name_label = LabelComponent(16, "Name: ")
         self.name_editor_label = LineEditComponent("Name")
         self.query_button = ButtonComponent("Query")
         self.del_button = ButtonComponent("Delete")
         self.hint = TextEditComponent()
         self.msg_box = MessageBoxComponent()

        #set grid
         self.layout.setColumnStretch(0, 1)
         self.layout.setColumnStretch(1, 2)
         self.layout.setColumnStretch(2, 1)
         self.layout.setColumnStretch(3, 4)
         self.layout.setRowStretch(0, 1)
         self.layout.setRowStretch(1, 1)
         self.layout.setRowStretch(2, 1)
         self.layout.setRowStretch(3, 5)

         #set widget position
         self.layout.addWidget(self.header_label, 0, 0, 1, 3)
         self.layout.addWidget(self.name_label, 1, 0, 1, 1)
         self.layout.addWidget(self.name_editor_label, 1, 1, 1, 1)
         self.layout.addWidget(self.query_button, 1, 2, 1, 1)
         self.layout.addWidget(self.del_button, 2, 0, 1, 3)
         self.layout.addWidget(self.hint,1, 3, 3, 1)

         self.query_button.clicked.connect(self.query_action)
         self.del_button.clicked.connect(self.del_action)
         self.name_editor_label.mousePressEvent = self.name_press_event

         self.setLayout(self.layout)
    
    def init_status(self):
        self.query_button.setEnabled(False)
        self.del_button.setEnabled(False)
        self.hint.setReadOnly(True)

    def query_action(self):
         if self.name_editor_label.text().strip() == "":
            self.hint.clear()
            self.hint.setText("Please input legitimate name")
         else: 
            self.send_command = ExecuteCommand(self.socket, "query", {'name': self.name_editor_label.text()})
            self.send_command.start()
            self.send_command.return_sig.connect(self.query_process_result)

    def query_process_result(self, result):
        result = json.loads(result)
        if result['status'] == 'OK':
            self.hint.clear()
            self.name = self.name_editor_label.text().strip()
            text = f"name: {self.name}\n"
            for subject, score in result['scores'].items():
                text += f"    {subject}: {score}\n"
            text += "\n"
            self.hint.setText(text)
            self.del_button.setEnabled(True)
        else:
            self.hint.setText(f"The {self.name_editor_label.text().strip()} is not exist")

    def del_action(self):
        user_reply = self.msg_box.show_message_box()
        if user_reply == 'Y':
            self.send_command = ExecuteCommand(self.socket, "delete", {'name': self.name})
            self.send_command.start()
            self.send_command.return_sig.connect(self.del_process_result)
        else:
            self.init_status()
            self.hint.clear()

    def del_process_result(self, result):
        result = json.loads(result) 
        self.init_status()
        self.hint.clear()
        if result['status'] == 'OK':
            self.hint.setText(f"{self.name} is already delete")
        else:
            self.hint.setText(f"error!! {self.name} is not delete")
            
    def name_press_event(self, event):
        self.query_button.setEnabled(True)
        self.name_editor_label.clear()

    def load(self):
        self.init_status()
        print("Del\n")
