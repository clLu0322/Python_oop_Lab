from PyQt6 import QtWidgets
import json
from ServiceController import ExecuteCommand
from WorkWidgets.WidgetComponents import (
    LabelComponent, 
    LineEditComponent, 
    ButtonComponent, 
    ScrollAreaComponent, 
    MessageQuestionBoxComponent
    )

class DelStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("del_stu_widget")
        layout = QtWidgets.QGridLayout()

        self.name_label = LabelComponent(16, "Name: ")
        self.name_editor_label = LineEditComponent("Name")
        self.query_button = ButtonComponent("Query")
        self.del_button = ButtonComponent("Delete")
        self.back_button = ButtonComponent("Back")
        self.hint_text = LabelComponent(16, "","black")
        self.hint_text.set_vertical_alignment("top")
        self.hint_scorll = ScrollAreaComponent(self.hint_text)
        self.msg_box = MessageQuestionBoxComponent()
        #set grid
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)
        layout.setColumnStretch(4, 4)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 6)
        layout.setRowStretch(2, 1)
        #set widget position
        layout.addWidget(self.name_label, 0, 0, 1, 1)
        layout.addWidget(self.name_editor_label, 0, 1, 1, 2)
        layout.addWidget(self.query_button, 0, 3, 1, 1)
        layout.addWidget(self.del_button, 2, 2, 1, 2)
        layout.addWidget(self.back_button, 2, 0, 1 ,2)
        layout.addWidget(self.hint_scorll, 0, 4, 3, 1)
        #set widget function
        self.query_button.clicked.connect(self.query_action)
        self.del_button.clicked.connect(self.del_action)
        self.name_editor_label.mousePressEvent = self.name_press_event
        self.back_button.mousePressEvent = self.back_press_event

        self.setLayout(layout)
    
    def init_status(self):
        self.query_button.setEnabled(False)
        self.del_button.setEnabled(False)
        self.name_editor_label.setEnabled(True)
        self.name_editor_label.setText("Name")
        self.hint_text.setText_Color("Please input the name.", "black")

    def query_action(self):
        if len(self.name_editor_label.text().strip()) == 0:
            self.hint_text.setText_Color("Please input legitimate name.", "red")
        else: 
            self.send_command = ExecuteCommand("query", {'name': self.name_editor_label.text().strip()})
            self.send_command.start()
            self.send_command.return_sig.connect(self.query_process_result)

    def query_process_result(self, result):
        result = json.loads(result)
        if result['status'] == 'OK':
            self.name = self.name_editor_label.text().strip()
            text = f"name: {self.name}\n"
            for subject, score in result['scores'].items():
                text += f"    {subject}: {score}\n"
            text += "\n"
            self.hint_text.setText_Color(text, "black")
            self.del_button.setEnabled(True)
            self.name_editor_label.setEnabled(False)
        else:
            self.hint_text.setText_Color(f"{result['reason']}", "red")

    def del_action(self):
        #彈窗確認使用者是否刪除
        user_reply = self.msg_box.show_message_box(f"Are you sure you want to delete {self.name}?")
        if user_reply:
            self.send_command = ExecuteCommand("delete", {'name': self.name})
            self.send_command.start()
            self.send_command.return_sig.connect(self.del_process_result)
        else:
            self.init_status()

    def del_process_result(self, result):
        result = json.loads(result) 
        self.init_status()
        if result['status'] == 'OK':
            self.hint_text.setText_Color(f"{self.name} is already delete.", "green")
        else:
            self.hint_text.setText_Color(f"error!! {self.name} is not delete", "red")
            
    def name_press_event(self, event):
        self.query_button.setEnabled(True)
        self.name_editor_label.clear()

    def back_press_event(self, event):
        self.init_status()

    def load(self):
        self.init_status()
