from PyQt6 import QtWidgets, QtCore, QtGui

class LabelComponent(QtWidgets.QLabel):
    def __init__(self, font_size, content, color="black"):
        super().__init__()
        self.setWordWrap(True)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.setStyleSheet(f"color: {color};")
        self.setFont(QtGui.QFont("Arial", pointSize=font_size, weight=500))
        self.setText(content)

class LineEditComponent(QtWidgets.QLineEdit):
    def __init__(self, default_content="", length=10, width=200, font_size=16):
        super().__init__()
        self.setMaxLength(length)
        self.setText(default_content)
        self.setMinimumHeight(30)
        self.setMaximumWidth(width)
        self.setFont(QtGui.QFont("Arial", font_size))

class ButtonComponent(QtWidgets.QPushButton):
    def __init__(self, text, font_size=16):
        super().__init__()
        self.setText(text)
        self.setFont(QtGui.QFont("Arial", font_size))

class TextEditComponent(QtWidgets.QTextEdit):
    def __init__(self, font_size=16):
        super().__init__()
        self.setFont(QtGui.QFont("Arial", font_size))

class ComboBoxConponent(QtWidgets.QComboBox):
    def __init__(self):
        super().__init__()
        # self.resize(300, 200)
        # self.setGeometry(10,10,200,30)

class MessageBoxComponent(QtWidgets.QMessageBox):
    def __init__(self, message="你確定要刪除嗎？", title="確認",font_size=16):
        super().__init__()
        self.setWindowTitle(title)
        self.setFont(QtGui.QFont("Arial", font_size))
        self.setText(message)
        self.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        self.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
    
    def show_message_box(self):
        user_response = self.exec()
        if user_response == QtWidgets.QMessageBox.StandardButton.Yes:
            return "Y"
        else:
            return "N"
        
class RadioButton(QtWidgets.QRadioButton):
    def __init__(self, text, font_size=14):
        super().__init__()
        self.setText(text)
        self.setFont(QtGui.QFont("Arial", font_size))

class ScrollAreaComponent(QtWidgets.QScrollArea):
    def __init__(self, content):
        super().__init__()
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.scroll_area_widget = QtWidgets.QWidget()  # 创建一个QWidget作为滚动区域的窗口部件
        self.scroll_area_layout = QtWidgets.QVBoxLayout(self.scroll_area_widget)  # 创建一个垂直布局管理器
        self.scroll_area_layout.addWidget(content)  # 将传入的内容添加到垂直布局中

        self.setWidget(self.scroll_area_widget)  # 将滚动区域窗口部件设置为滚动区域的可滚动部件




        
