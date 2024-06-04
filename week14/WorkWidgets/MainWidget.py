from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.AddStuWidget import AddStuWidget
from WorkWidgets.ShowStuWidget import ShowStuWidget
from WorkWidgets.DelStuWidget import DelStuWidget
from WorkWidgets.ModifyStuWidget import ModifyStuWidget
from WorkWidgets.WidgetComponents import LabelComponent


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("main_widget")
        layout = QtWidgets.QGridLayout()
        header_label = LabelComponent(24, "Student Management System")
        header_label.set_font_weight(1000)
        header_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.function_widget = FunctionWidget()

        layout.addWidget(header_label, 0, 0, 1, 4)
        layout.addWidget(self.function_widget, 1, 0, 1, 4)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 7)

        self.setLayout(layout)
        self.setStyleSheet("#main_widget { background-color: pink; }")

class FunctionWidget(QtWidgets.QTabWidget):
    def __init__(self):
        super().__init__()

        self.welcome_label = LabelComponent(72, "Welcome")
        self.welcome_label.set_font_weight(1000)
        self.welcome_label.setStyleSheet("background-color: pink;")

        self.prompt_label = LabelComponent(32, "Click to enter", color="gray")
        self.welcome_widget = QtWidgets.QWidget()
        self.welcome_layout = QtWidgets.QVBoxLayout(self.welcome_widget)
        self.welcome_layout.addStretch(1)
        self.welcome_layout.addWidget(self.welcome_label, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.welcome_layout.addWidget(self.prompt_label, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.welcome_layout.addStretch(1)
        self.welcome_widget.setLayout(self.welcome_layout)

        self.addTab(self.welcome_widget, "")

        self.addTab(AddStuWidget(), "Add student")
        self.addTab(ShowStuWidget(), "Show all")
        self.addTab(DelStuWidget(), "Del student")
        self.addTab(ModifyStuWidget(), "Mod student")

        self.set_tab_font(20)
        self.set_welcome_tab_color()

        self.tabBar().setVisible(False)

        self.currentChanged.connect(self.on_tab_changed)
        self.widget_dict = {
            "Add student": self.widget(1),
            "Show all": self.widget(2),
            "Del student": self.widget(3),
            "Mod student": self.widget(4),
        }
        # 設置歡迎標籤點擊事件
        self.welcome_label.mousePressEvent = self.show_tabs

    def on_tab_changed(self, index):
        current_widget = self.widget(index)
        if hasattr(current_widget, 'load'):
            current_widget.load()
        print(f"Switched to {self.tabText(index)} tab")
        self.restore_tab_color()

    def set_tab_font(self, font_size):
        font = QtGui.QFont()
        font.setPointSize(font_size)
        self.setFont(font)

    def set_welcome_tab_color(self):
        self.setStyleSheet(f"""
        QTabWidget::pane {{
            border: 1px solid pink;
            top: 0px;
            background: pink;
        }}
        QTabBar::tab {{
            background: deepskyblue;
            padding: 10px;
            color: white;
        }}
        QTabBar::tab:selected, QTabBar::tab:hover {{
            background: royalblue;
            color: yellow;
        }}
        QTabBar::tab:selected {{
            border-color: pink;
        }}
        """)

    def restore_tab_color(self):
        self.setStyleSheet(f"""
        QTabWidget::pane {{
            border: 1px solid royalblue;
            top: 0px;
            background: royalblue;
        }}
        QTabBar::tab {{
            background: deepskyblue;
            padding: 10px;
            color: white;
        }}
        QTabBar::tab:selected, QTabBar::tab:hover {{
            background: royalblue;
            color: yellow;
        }}
        QTabBar::tab:selected {{
            border-color: skyblue;
        }}
        """)

    def show_tabs(self, event):
        self.tabBar().setVisible(True)
        self.removeTab(0)  # 移除歡迎標籤
        self.setCurrentIndex(0)
        self.restore_tab_color()
