from PyQt6 import QtWidgets
from WorkWidgets.AddStuWidget import AddStuWidget
from WorkWidgets.ShowStuWidget import ShowStuWidget
from WorkWidgets.DelStuWidget import DelStuWidget
from WorkWidgets.ModifyStuWidget import ModifyStuWidget
from WorkWidgets.WidgetComponents import LabelComponent
from WorkWidgets.WidgetComponents import ButtonComponent


class MainWidget(QtWidgets.QWidget):
    def __init__(self, socket):
        super().__init__()
        self.setObjectName("main_widget")

        layout = QtWidgets.QGridLayout()
        header_label = LabelComponent(24, "Student Management System")
        function_widget = FunctionWidget(socket)
        menu_widget = MenuWidget(function_widget.update_widget)

        layout.addWidget(header_label, 0, 0, 1, 3)
        layout.addWidget(menu_widget, 1, 0, 1, 4)
        layout.addWidget(function_widget, 2, 0, 1, 4)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 6)

        self.setLayout(layout)

class MenuWidget(QtWidgets.QWidget):
    def __init__(self, update_widget_callback):
        super().__init__()
        self.setObjectName("menu_widget")
        self.update_widget_callback = update_widget_callback

        layout = QtWidgets.QHBoxLayout()
        add_button = ButtonComponent("Add student")
        show_button = ButtonComponent("Show all")
        del_button = ButtonComponent("Del student")
        modify_button = ButtonComponent("Mod student")
        # https://medium.com/seaniap/python-lambda-函式-7e86a56f1996
        add_button.clicked.connect(lambda: self.update_widget_callback("add"))
        show_button.clicked.connect(lambda: self.update_widget_callback("show"))
        del_button.clicked.connect(lambda: self.update_widget_callback("del"))
        modify_button.clicked.connect(lambda: self.update_widget_callback("modify"))
        
        layout.addWidget(add_button, stretch=1)
        layout.addWidget(del_button, stretch=1)
        layout.addWidget(modify_button, stretch=1)
        layout.addWidget(show_button, stretch=1)

        self.setLayout(layout)


class FunctionWidget(QtWidgets.QStackedWidget):
    def __init__(self,socket):
        super().__init__()
        self.widget_dict = {
            "add": self.addWidget(AddStuWidget(socket)),
            "show": self.addWidget(ShowStuWidget(socket)),
            "del": self.addWidget(DelStuWidget(socket)),
            "modify": self.addWidget(ModifyStuWidget(socket)), 
        }
        self.update_widget("add")
    
    def update_widget(self, name):
        self.setCurrentIndex(self.widget_dict[name])
        current_widget = self.currentWidget()
        current_widget.load()