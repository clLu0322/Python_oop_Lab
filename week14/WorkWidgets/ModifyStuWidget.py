from PyQt6 import QtWidgets
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
         self.layout = QtWidgets.QGridLayout()

         self.header_label = LabelComponent(20, "Modify Student")
         self.name_label = LabelComponent(16, "Name: ")
         self.subject_label = LabelComponent(16, "Subject: ")
         self.name_editor_label = LineEditComponent("Name")
         self.subject_combobox = ComboBoxConponent(['+'])
         self.query_button = ButtonComponent("Query")
         self.hint = TextEditComponent()
         self.add_option = RadioButton("Add")
         self.modify_option = RadioButton("Modify")

        #set grid
         self.layout.setColumnStretch(0, 1)
         self.layout.setColumnStretch(1, 1)
         self.layout.setColumnStretch(2, 1)
         self.layout.setColumnStretch(3, 1)
         self.layout.setColumnStretch(4, 4)

         self.layout.setRowStretch(0, 1)
         self.layout.setRowStretch(1, 1)
         self.layout.setRowStretch(2, 1)
         self.layout.setRowStretch(3, 1)
         self.layout.setRowStretch(4, 4)

         #set widget position
         self.layout.addWidget(self.header_label, 0, 0, 1, 3)
         self.layout.addWidget(self.name_label, 1, 0, 1, 1)
         self.layout.addWidget(self.subject_label, 2, 0, 1, 1)
         self.layout.addWidget(self.name_editor_label, 1, 1, 1, 2)
         self.layout.addWidget(self.query_button, 1, 3, 1, 1)
         self.layout.addWidget(self.hint,1, 4, 4, 1)

         self.layout.addWidget(self.subject_combobox,2, 1, 1, 2)
         self.layout.addWidget(self.add_option, 0, 2, 1, 1)
         self.layout.addWidget(self.modify_option, 0, 3, 1, 1)

         self.query_button.clicked.connect(self.query_action)
         self.name_editor_label.mousePressEvent = self.name_press_event

         self.setLayout(self.layout)
    
    def init_status(self):
         self.hint.setReadOnly(True)
         self.query_button.setEnabled(False)
         self.name_editor_label

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
        if result['message']['status'] == 'OK':
            self.hint.clear()
            text = f"name: {self.name_editor_label.text().strip()}\n"
            for subject, score in result['message']['scores'].items():
                text += f"    {subject}: {score}\n"
            text += "\n"
            self.hint.setText(text)
        else:
            self.hint.setText("error")


    
    def name_press_event(self, event):
        self.query_button.setEnabled(True)
        self.name_editor_label.clear()

    def load(self):
        self.init_status()
        print("Mod")
