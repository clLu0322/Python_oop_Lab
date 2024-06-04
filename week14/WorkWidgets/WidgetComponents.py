from PyQt6 import QtWidgets, QtCore, QtGui


class LabelComponent(QtWidgets.QLabel):
    def __init__(self, font_size, content, color="black", background_color=None):
        super().__init__()
        self.setWordWrap(True)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.setStyleSheet(f"color: {color};")
        if background_color:
            self.setStyleSheet(self.styleSheet() + f" background-color: {background_color};")
        font = QtGui.QFont("Arial", pointSize=font_size)
        font_weight = QtGui.QFont.Weight.Normal
        font.setWeight(font_weight)
        self.setFont(font)
        self.setText(content)
    
    def setText_Color(self, text, color):
        self.setText(text)
        self.setStyleSheet(f"color: {color};")
    
    def set_font_weight(self, font_weight):
        # 改字粗細
        font = self.font()
        font.setWeight(font_weight)
        self.setFont(font)
    
    def set_vertical_alignment(self, vertical):
        alignment = QtCore.Qt.AlignmentFlag.AlignLeft
        if vertical == "top":
            alignment |= QtCore.Qt.AlignmentFlag.AlignTop
        elif vertical == "bottom":
            alignment |= QtCore.Qt.AlignmentFlag.AlignBottom
        elif vertical == "center":
            alignment |= QtCore.Qt.AlignmentFlag.AlignVCenter
        self.setAlignment(alignment)
    
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
        self.setStyleSheet(f"""
            QPushButton {{
                border-radius: 15px;
                background-color: deepskyblue;
                color: yellow;
                padding: 10px 24px;
                text-align: center;
                font-size: {font_size}px;
                font-weight: bold;  /* 加粗字體 */
                min-width: 50px;
                min-height: 20px;
            }}
            QPushButton:pressed {{
                background-color: royalblue;
                border: 2px solid deepskyblue;
            }}
            QPushButton:disabled {{
                background-color: lightgray;  
                color: gray;  
                border: 2px solid darkgray;
                font-weight: bold;  /* 加粗字體 */
            }}
        """)

class ComboBoxConponent(QtWidgets.QComboBox):
    def __init__(self,font_size=16):
        super().__init__()
        self.setFont(QtGui.QFont("Arial", font_size))

class MessageQuestionBoxComponent(QtWidgets.QMessageBox):
    def __init__(self, title="確認",font_size=16):
        super().__init__()
        self.setWindowTitle(title)
        self.setFont(QtGui.QFont("Arial", font_size))
        self.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        self.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)
    
    def show_message_box(self, message):
        self.setText(message)
        user_response = self.exec()
        if user_response == QtWidgets.QMessageBox.StandardButton.Yes:
            return True
        else:
            return False
        
class RadioButton(QtWidgets.QRadioButton):
    def __init__(self, text, font_size=16):
        super().__init__()
        self.setText(text)
        self.setFont(QtGui.QFont("Arial", font_size))

class ScrollAreaComponent(QtWidgets.QScrollArea):
    def __init__(self, content):
        super().__init__()
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.scroll_area_widget = QtWidgets.QWidget()
        self.scroll_area_layout = QtWidgets.QVBoxLayout(self.scroll_area_widget)
        self.scroll_area_layout.setContentsMargins(0, 0, 0, 0)  # 設置邊距為 0
        self.scroll_area_layout.addWidget(content)
        self.setWidget(self.scroll_area_widget)





        
