from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QIntValidator
import json
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent
from ServerController import ExecuteCommand

class AddStuWidget(QtWidgets.QWidget):
    def __init__(self, socket):
        super().__init__()
        self.socket = socket
        self.student_dict = {'name': "", 'scores':{}}
        self.setObjectName("add_stu_widget")
        self.layout = QtWidgets.QGridLayout()
        #label init
        self.hint_text =LabelComponent(16, "Welcome", color="red")
        self.header_label = LabelComponent(20, "Add Student")
        self.name_label = LabelComponent(16, "Name: ")
        self.subject_Label = LabelComponent(16, "Subject: ")
        self.score_Label = LabelComponent(16, "Score: ")
        #editor init
        self.editor_label_name = LineEditComponent("Name")
        self.editor_label_subject = LineEditComponent("Subject")
        self.editor_label_score = LineEditComponent("")
        #button init
        self.button_query = ButtonComponent("Query")
        self.button_add = ButtonComponent("Add")
        self.button_send = ButtonComponent("Send")
    
        self.set_grid()
        self.set_widget_position()
        self.set_widget_function()
        self.widget_status_init()

        self.setLayout(self.layout)

    def set_widget_position(self):
        self.layout.addWidget(self.hint_text, 0, 3, 3, 1)
        self.layout.addWidget(self.header_label, 0, 0, 1, 2)
        self.layout.addWidget(self.name_label, 1, 0, 1, 1)
        self.layout.addWidget(self.subject_Label, 2, 0, 1, 1)
        self.layout.addWidget(self.score_Label, 3, 0, 1, 1)
        self.layout.addWidget(self.editor_label_name, 1, 1, 1, 1)
        self.layout.addWidget(self.editor_label_subject, 2, 1, 1, 1)
        self.layout.addWidget(self.editor_label_score, 3, 1, 1, 1)
        self.layout.addWidget(self.button_query, 1, 2, 1, 1)
        self.layout.addWidget(self.button_add, 3, 2, 1, 1)
        self.layout.addWidget(self.button_send,  5, 3, 1, 1)
    
    def set_grid(self):
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 4)
        self.layout.setColumnStretch(2, 1)
        self.layout.setColumnStretch(3, 4)
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 5)
        self.layout.setRowStretch(2, 5)
        self.layout.setRowStretch(3, 5)
        self.layout.setRowStretch(4, 5)
        self.layout.setRowStretch(5, 1)   

    def set_widget_function(self):
        #設定button功能
        self.button_query.clicked.connect(self.query_action)
        self.button_add.clicked.connect(self.add_action)
        self.button_send.clicked.connect(self.send_action)
        #設定score輸入限制
        self.editor_label_score.setMaxLength(3)
        self.editor_label_score.setValidator(QIntValidator())
        #設定滑鼠點擊事件
        self.editor_label_name.mousePressEvent = self.name_press_event 
        self.editor_label_subject.mousePressEvent = self.subject_press_event
        self.editor_label_score.mousePressEvent = self.score_press_event 
    
    def widget_status_init(self):
        #初始化部件狀態
        self.set_editor_status('name', True)
        self.set_editor_status('subject', False)
        self.set_editor_status('score', False)
        self.set_button_status('query', False)
        self.set_button_status('add', False)
        self.set_button_status('send', False)


    def query_action(self):
        #如果沒輸入，提示使用者
        if self.editor_label_name.text() == "":
            self.hint_text.setText("Please input legitimate name")
        else:
            self.send_command = ExecuteCommand(self.socket, "query", {'name': self.editor_label_name.text()})
            self.send_command.start()
            self.send_command.return_sig.connect(self.query_process_result)

    def query_process_result(self, result):
        result = json.loads(result)
        if result['message']['status'] == 'Fail':
            self.set_editor_status('name', False)
            self.set_editor_status('subject', True)
            self.set_editor_status('score', True)
            self.set_button_status('add', True)
            self.set_button_status('query', False)
            self.hint_text.setText(f"Please input {self.editor_label_name.text()}'s subject and score")
        else:
            self.hint_text.setText(f"{self.editor_label_name.text()} already exists")

    def add_action(self):
        if self.editor_label_subject.text() == "" or self.editor_label_score.text() == "":
            #如果輸入為空，則提示
            self.hint_text.setText("Please input legitimate subject and score") 
        elif self.editor_label_subject.text() in self.student_dict['scores'].keys():
            #科目已經輸入過了
            self.hint_text.setText(f"{self.editor_label_subject.text()} already in information") 
        else:
            self.student_dict['name'] = self.editor_label_name.text()
            self.student_dict['scores'].update({self.editor_label_subject.text(): self.editor_label_score.text()})
            self.hint_text.setText(f"Add {self.editor_label_name.text()}'s information\n"
                                   f"{self.editor_label_subject.text()}:{self.editor_label_score.text()}\n"
                                   f"current information\n{self.student_dict} ")
            self.set_button_status('send', True)

    def send_action(self):
        self.send_command = ExecuteCommand(self.socket, "add", self.student_dict)
        self.send_command.start()
        self.send_command.return_sig.connect(self.send_process_result)
        
    def send_process_result(self, result):
        result = json.loads(result)
        if result['message']['status'] == 'OK':
            self.hint_text.setText(f"Send {self.student_dict} success")
            #reset student_dict
            self.student_dict = {"name": "", "scores": {}}
            #設定部件狀態
            self.widget_status_init()
            self.set_button_status('query', True)
        else:
            self.hint_text.setText(f"Send {self.student_dict} fail")
            
    def set_button_status(self, button, status):
        if button == 'add':
            self.button_add.setEnabled(status)
        elif button == 'send':
            self.button_send.setEnabled(status)
        elif button == 'query':
            self.button_query.setEnabled(status)

    def set_editor_status(self, editor, status):
        if editor == 'name':
            self.editor_label_name.setEnabled(status)
        elif editor == 'subject':
            self.editor_label_subject.setEnabled(status)
        elif editor == 'score':
            self.editor_label_score.setEnabled(status)

    def name_press_event(self, event):
        self.set_button_status('query', True)
        self.editor_label_name.clear()
    
    def subject_press_event(self, event):
        self.set_button_status('add', True)
        self.editor_label_subject.clear()
    
    def score_press_event(self, event):
        self.editor_label_score.clear()
