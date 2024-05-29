from PyQt6 import QtWidgets
from PyQt6.QtGui import QIntValidator
import json
from ServiceController import ExecuteCommand
from WorkWidgets.WidgetComponents import (
    LabelComponent, 
    LineEditComponent, 
    ButtonComponent, 
    TextEditComponent, 
    ComboBoxConponent,
    RadioButton
)

class ModifyStuWidget(QtWidgets.QWidget):
    def __init__(self, socket):
        super().__init__()
        self.socket = socket
        self.setObjectName("modify_stu_widget")
        self.parameters = {}  
        layout = QtWidgets.QGridLayout()

        self.header_label = LabelComponent(20, "Modify Student")
        self.name_label = LabelComponent(16, "Name: ")
        self.name_editor_label = LineEditComponent("Name")
        self.subject_label = LabelComponent(16, "Subject: ")
        self.subject_editor_label = LineEditComponent("Subject")
        self.subject_combobox = ComboBoxConponent()
        self.score_label = LabelComponent(16, "Score: ")
        self.score_editor_label = LineEditComponent("")
        self.query_button = ButtonComponent("Query")
        self.add_button = ButtonComponent("Add")
        self.send_button = ButtonComponent("Send")
        self.hint = TextEditComponent()
        self.add_option = RadioButton("Add")
        self.modify_option = RadioButton("Modify")

        # 設置網格佈局
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)
        layout.setColumnStretch(4, 4)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 1)
        layout.setRowStretch(4, 1)
        layout.setRowStretch(5, 2)
        layout.setRowStretch(6, 1)

        # 設置控件位置
        layout.addWidget(self.header_label, 0, 0, 1, 2)
        layout.addWidget(self.name_label, 1, 0, 1, 1)
        layout.addWidget(self.name_editor_label, 1, 1, 1, 2)
        layout.addWidget(self.query_button, 1, 3, 1, 1)
        layout.addWidget(self.hint, 1, 4, 5, 1)
        layout.addWidget(self.add_option, 2, 0, 1, 1)
        layout.addWidget(self.modify_option, 2, 2, 1, 1)
        layout.addWidget(self.subject_editor_label, 3, 1, 1, 2)
        layout.addWidget(self.subject_combobox, 3, 1, 1, 2)
        layout.addWidget(self.subject_label, 3, 0, 1, 1)
        layout.addWidget(self.score_label, 4, 0, 1, 1)
        layout.addWidget(self.score_editor_label, 4, 1, 1, 2)
        layout.addWidget(self.add_button, 4, 3 ,1, 1)
        layout.addWidget(self.send_button, 6, 0, 1, 4)
        

        self.hint.setReadOnly(True)
        self.query_button.clicked.connect(self.query_action)
        self.add_button.clicked.connect(self.add_action)
        self.send_button.clicked.connect(self.send_action)
        self.score_editor_label.setMaxLength(3)
        self.score_editor_label.setValidator(QIntValidator())
        self.name_editor_label.mousePressEvent = self.name_press_event
        self.subject_editor_label.mousePressEvent = self.subject_press_event
        self.score_editor_label.mousePressEvent = self.score_press_event

        self.setLayout(layout)
    
    def init_status(self):
        self.query_button.setEnabled(False)
        self.name_editor_label.clear()
        self.subject_editor_label.hide()
        self.subject_label.hide()
        self.score_label.hide()
        self.score_editor_label.hide()
        self.subject_combobox.hide()
        self.add_button.hide()
        self.send_button.hide()
        self.add_option.setChecked(True)
        self.modify_option.setChecked(False)
        self.subject_combobox.clear()
    
    def query_action(self):
        if len(self.name_editor_label.text()) == 0:
            self.hint.setText("Please input legitimate name")
        else: 
            self.send_command = ExecuteCommand(self.socket, "query", {'name': self.name_editor_label.text()})
            self.send_command.start()
            self.send_command.return_sig.connect(self.query_process_result)

    def query_process_result(self, result):
        result = json.loads(result)
        if result['message']['status'] == 'OK':
            self.name = self.name_editor_label.text().strip()
            self.parameters = result['message']['scores']
            self.hint.clear()

            text = f"name: {self.name}\n"
            for subject, score in self.parameters.items():
                text += f"    {subject}: {score}\n"
                self.subject_combobox.addItem(subject)
            text += "\n"
            self.hint.setText(text)
            self.subject_label.show()
            self.score_editor_label.show()
            self.score_label.show()
            
            self.send_button.show()

            if self.add_option.isChecked():
                self.subject_editor_label.show()
                self.add_button.show()
            else:
                self.subject_combobox.show()

    def add_action(self):
        if len(self.subject_editor_label.text())== 0 or len(self.score_editor_label.text()) == 0:
            self.hint("Please input legitimate subject and score")
        elif self.subject_editor_label.text() in self.parameters.keys():
            self.hint.setText("please input new subject")
        else: 
            self.parameters[self.subject_editor_label.text()] = self.score_editor_label.text()

    def send_action(self):
        self.send_command = ExecuteCommand(self.socket, "modify", {'name':self.name, 'scores':self.parameters})
        self.send_command.start()
        self.send_command.return_sig.connect(self.send_process_result)
    
    def send_process_result(self, result):
        result = json.loads(result)
        if result['message']['status'] == 'OK':
            self.hint.setText("Send success")
            self.init_status()
        else:
            self.hint.setText("Send fail")

    def name_press_event(self, event):
        self.query_button.setEnabled(True)
        self.name_editor_label.clear()

    def subject_press_event(self, event):
         self.subject_editor_label.clear()

    def score_press_event(self, event):
         self.score_editor_label.clear()

    def load(self):
        self.init_status()
        print("Mod")