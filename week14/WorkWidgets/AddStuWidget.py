from PyQt6 import QtWidgets
from PyQt6.QtGui import QIntValidator
from ServiceController import ExecuteCommand
import json
from WorkWidgets.WidgetComponents import (
    LabelComponent, 
    LineEditComponent, 
    ButtonComponent, 
    ScrollAreaComponent)

class AddStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.student_dict = {'name': "", 'scores':{}}
        self.setObjectName("add_stu_widget")
        layout = QtWidgets.QGridLayout()
        layout.setSpacing(10)
        #label init
        self.hint_text = LabelComponent(16, "")
        self.hint_text.set_vertical_alignment("top")
        self.hint_scorll = ScrollAreaComponent(self.hint_text)
        self.name_label = LabelComponent(16, "Name: ")
        self.subject_label = LabelComponent(16, "Subject: ")
        self.score_label = LabelComponent(16, "Score: ")
        #editor init
        self.name_editor_label = LineEditComponent("Name")
        self.subject_editor_label = LineEditComponent("Subject")
        self.score_editor_label = LineEditComponent("")
        #button init
        self.query_button = ButtonComponent("Query")
        self.add_button = ButtonComponent("Add")
        self.send_button = ButtonComponent("Send")
        self.back_button = ButtonComponent("Back")

        #set position
        layout.addWidget(self.hint_scorll, 0, 4, 5, 1)
        layout.addWidget(self.name_label, 0, 0, 1, 1)
        layout.addWidget(self.subject_label, 1, 0, 1, 1)
        layout.addWidget(self.score_label, 2, 0, 1, 1)
        layout.addWidget(self.name_editor_label, 0, 1, 1, 2)
        layout.addWidget(self.subject_editor_label, 1, 1, 1, 2)
        layout.addWidget(self.score_editor_label, 2, 1, 1, 2)
        layout.addWidget(self.query_button, 0, 3, 1, 1)
        layout.addWidget(self.add_button, 2, 3, 1, 1)
        layout.addWidget(self.back_button, 4, 0, 1, 2)
        layout.addWidget(self.send_button,  4, 2, 1, 2)
        #set grid
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)
        layout.setColumnStretch(4, 4)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 3)
        layout.setRowStretch(4, 1) 
        self.init_status()


        #設定button功能
        self.query_button.clicked.connect(self.query_action)
        self.add_button.clicked.connect(self.add_action)
        self.send_button.clicked.connect(self.send_action)
        self.back_button.clicked.connect(self.back_action)
        #設定score輸入限制
        self.score_editor_label.setMaxLength(3)
        self.score_editor_label.setValidator(QIntValidator())
        #設定滑鼠點擊事件
        self.name_editor_label.mousePressEvent = self.name_press_event 
        self.subject_editor_label.mousePressEvent = self.subject_press_event
        self.score_editor_label.mousePressEvent = self.score_press_event 
        self.setLayout(layout)
    
    def init_status(self):
        #初始化部件狀態
        self.student_dict = {"name": "", "scores": {}}
        self.name_editor_label.setEnabled(True)
        self.subject_editor_label.setEnabled(False)
        self.score_editor_label.setEnabled(False)
        self.query_button.setEnabled(False)
        self.add_button.setEnabled(False)
        self.send_button.setEnabled(False)
        self.name_editor_label.setText("Name")
        self.subject_editor_label.setText("Subject")
        self.score_editor_label.setText("")
        self.hint_text.setText_Color("Please input the new name", "black")

    def query_action(self):
        #如果沒輸入，提示使用者
        if len(self.name_editor_label.text().strip()) == 0:
            self.hint_text.setText_Color("Please input legitimate name", "red")
        else:
            self.send_command = ExecuteCommand("query", {'name': self.name_editor_label.text().strip()})
            self.send_command.start()
            self.send_command.return_sig.connect(self.query_process_result)

    def query_process_result(self, result):
        result = json.loads(result)
        if result['status'] == 'Fail':
            self.name_editor_label.setEnabled(False)
            self.subject_editor_label.setEnabled(True)
            self.score_editor_label.setEnabled(True)
            self.add_button.setEnabled(True)
            self.query_button.setEnabled(False)
            self.hint_text.setText_Color(f"Please input {self.name_editor_label.text().strip()}'s subject and score.", "green")
        else:
            self.hint_text.setText_Color("The name is already exist.", "red")

    def add_action(self):
        if len(self.subject_editor_label.text().strip()) == 0 or len(self.score_editor_label.text()) == 0:
            #如果輸入為空，則提示
            self.hint_text.setText_Color("Please input legitimate subject and score.", "red") 
        elif self.subject_editor_label.text().strip() in self.student_dict['scores'].keys():
            #科目已經輸入過了
            self.hint_text.setText_Color(f"{self.subject_editor_label.text().strip()} already in information", "red") 
        else:
            self.student_dict['name'] = self.name_editor_label.text().strip()
            self.student_dict['scores'].update({self.subject_editor_label.text().strip(): self.score_editor_label.text()})
            for key, value in self.student_dict.items():
                if key == 'name':
                    text = f"Name: {value}"
                else:
                    for subject, score in value.items():
                        text += f"    subject: {subject}, score:{score}\n"
                text += "\n"
            self.hint_text.setText_Color(text,"black")
            self.send_button.setEnabled(True)

    def send_action(self):
        self.send_command = ExecuteCommand("add", self.student_dict)
        self.send_command.start()
        self.send_command.return_sig.connect(self.send_process_result)
        
    def send_process_result(self, result):
        result = json.loads(result)
        if result['status'] == 'OK':
            self.hint_text.setText_Color(f"Send success", "green")
            self.init_status()
        else:
            self.hint_text.setText_Color(f"Send {self.student_dict} fail", "green")
            self.init_status()
    
    def back_action(self):
        self.init_status()

    def name_press_event(self, event):
        self.query_button.setEnabled(True)
        self.name_editor_label.clear()
    
    def subject_press_event(self, event):
        self.add_button.setEnabled(True)
        self.subject_editor_label.clear()
    
    def score_press_event(self, event):
        self.score_editor_label.clear()

    def load(self):
        self.init_status()
        