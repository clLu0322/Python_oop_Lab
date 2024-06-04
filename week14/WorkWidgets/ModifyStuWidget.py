from PyQt6 import QtWidgets
from PyQt6.QtGui import QIntValidator
import json
from ServiceController import ExecuteCommand
from WorkWidgets.WidgetComponents import (
    LabelComponent, 
    LineEditComponent, 
    ButtonComponent,  
    ComboBoxConponent,
    RadioButton,
    ScrollAreaComponent
)

class ModifyStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("modify_stu_widget")
        self.parameters = {}  
        layout = QtWidgets.QGridLayout()

        self.name_label = LabelComponent(16, "Name: ")
        self.name_editor_label = LineEditComponent("Name")
        self.subject_label = LabelComponent(16, "Subject: ")
        self.subject_editor_label = LineEditComponent("Subject")
        self.subject_combobox = ComboBoxConponent()
        self.score_label = LabelComponent(16, "Score: ")
        self.score_editor_label = LineEditComponent("")
        self.query_button = ButtonComponent("Query")
        self.back_button = ButtonComponent("Back")
        self.send_button = ButtonComponent("Send")
        self.hint_text = LabelComponent(14, "")
        self.hint_text.set_vertical_alignment("top")
        self.hint_scroll = ScrollAreaComponent(self.hint_text)
        self.add_radiobutton = RadioButton("Add")
        self.modify_radiobutton = RadioButton("Modify")

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)
        layout.setColumnStretch(4, 4)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 1)
        layout.setRowStretch(3, 1)
        layout.setRowStretch(4, 3)
        layout.setRowStretch(5, 1)

        layout.addWidget(self.name_label, 0, 0, 1, 1)
        layout.addWidget(self.name_editor_label, 0, 1, 1, 2)
        layout.addWidget(self.query_button, 0, 3, 1, 1)
        layout.addWidget(self.hint_scroll, 0, 4, 6, 1)
        layout.addWidget(self.add_radiobutton, 1, 0, 1, 1)
        layout.addWidget(self.modify_radiobutton, 1, 2, 1, 1)
        layout.addWidget(self.subject_editor_label, 2, 1, 1, 2)
        layout.addWidget(self.subject_combobox, 2, 1, 1, 2)
        layout.addWidget(self.subject_label, 2, 0, 1, 1)
        layout.addWidget(self.score_label, 3, 0, 1, 1)
        layout.addWidget(self.score_editor_label, 3, 1, 1, 2)
        layout.addWidget(self.back_button, 5, 0 ,1, 2)
        layout.addWidget(self.send_button, 5, 2, 1, 2)

        self.query_button.clicked.connect(self.query_action)
        self.back_button.clicked.connect(self.init_status)
        self.send_button.clicked.connect(self.send_action)
        self.score_editor_label.setMaxLength(3)
        self.score_editor_label.setValidator(QIntValidator())
        self.name_editor_label.mousePressEvent = self.name_press_event
        self.subject_editor_label.mousePressEvent = self.subject_press_event
        self.score_editor_label.mousePressEvent = self.score_press_event
        self.add_radiobutton.toggled.connect(self.radio_button_toggled)
        self.modify_radiobutton.toggled.connect(self.radio_button_toggled)

        self.setLayout(layout)
    
    def init_status(self):
        self.query_button.setEnabled(False)
        self.name_editor_label.clear()
        self.name_editor_label.setEnabled(True)
        self.subject_label.hide()
        self.subject_editor_label.hide()
        self.subject_combobox.hide()
        self.subject_combobox.clear()
        self.score_label.hide()
        self.score_editor_label.hide()
        self.back_button.hide()
        self.send_button.hide()
        self.add_radiobutton.hide()
        self.modify_radiobutton.hide()
        self.hint_text.setText_Color("Please enter a name whose subject you want to modify.", "black")
        
    
    def query_action(self):
        if len(self.name_editor_label.text()) == 0:
            self.hint_text.setText_Color("Please input legitimate name.", "red")
        else: 
            self.send_command = ExecuteCommand("query", {'name': self.name_editor_label.text()})
            self.send_command.start()
            self.send_command.return_sig.connect(self.query_process_result)

    def query_process_result(self, result):
        result = json.loads(result)
        if result['status'] == 'OK':
            self.name = self.name_editor_label.text().strip()
            self.parameters = result['scores']
            self.hint_text.setText_Color("Please choose the option add or moidify.", "green")
            self.name_editor_label.setEnabled(False)
            self.query_button.setEnabled(False)
            self.add_radiobutton.show()
            self.modify_radiobutton.show()
        else:
            self.hint_text.setText_Color("The name is not found.", "red")

    def send_action(self):
        if self.add_radiobutton.isChecked():
            if len(self.subject_editor_label.text()) == 0 or len(self.score_editor_label.text()) == 0:
                self.hint_text.setText_Color("Please input legitimate subject and score.", "red")
            elif self.subject_editor_label.text() in self.parameters.keys():
                self.hint_text.setText_Color("Please input new subject", "red")
            else: 
                self.parameters[self.subject_editor_label.text()] = self.score_editor_label.text()
                self.send_command = ExecuteCommand("modify", {'name':self.name, 'scores':self.parameters})
                self.send_command.start()
                self.send_command.return_sig.connect(self.send_process_result)

        elif self.modify_radiobutton.isChecked():
            if len(self.score_editor_label.text()) == 0:
                self.hint_text.setText_Color("Please input legitimate subject and score.", "red")
            else:
                self.parameters[self.subject_combobox.currentText()] = self.score_editor_label.text()
                self.send_command = ExecuteCommand("modify", {'name':self.name, 'scores':self.parameters})
                self.send_command.start()
                self.send_command.return_sig.connect(self.send_process_result)
        
    def send_process_result(self, result):
        result = json.loads(result)
        if self.add_radiobutton.isChecked():
            if result['status'] == 'OK':
                self.hint_text.setText_Color("Add success.", "green")
            else:
                self.hint_text.setText("Add fail.", "red")
                del self.parameters[self.subject_editor_label.text()]
        elif self.modify_radiobutton.isChecked():
            if result['status'] == 'OK':
                self.hint_text.setText_Color("Modify success.", "green")
            else:
                self.hint_text.setText_Color("Modify fail.", "red")
                del self.parameters[self.subject_combobox.currentText()]

    def radio_button_toggled(self):
        self.subject_label.show()
        self.score_label.show()
        self.score_editor_label.show()
        self.back_button.show()
        self.send_button.show()
        if self.add_radiobutton.isChecked():
                self.subject_editor_label.show()
                self.subject_combobox.hide()
                self.subject_combobox.clear()
                text = f"name: {self.name}\n"
                for subject, score in self.parameters.items():
                    text += f"    {subject}: {score}\n"
                text += "\n"
                self.hint_text.setText_Color(text,"black")

        elif self.modify_radiobutton.isChecked():
                self.subject_editor_label.hide()
                self.subject_combobox.show()
                self.subject_combobox.clear()
                text = f"name: {self.name}\n"
                for subject, score in self.parameters.items():
                    text += f"    {subject}: {score}\n"
                    self.subject_combobox.addItem(subject)
                text += "\n"
                self.hint_text.setText_Color(text,"black")

    def name_press_event(self, event):
        self.query_button.setEnabled(True)
        self.name_editor_label.clear()

    def subject_press_event(self, event):
         self.subject_editor_label.clear()

    def score_press_event(self, event):
         self.score_editor_label.clear()

    def load(self):
        self.init_status()
