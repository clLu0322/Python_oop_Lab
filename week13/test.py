import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QScrollBar 
from PyQt6.QtCore import Qt 
class ScrollTextWindow(QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle("Scroll Text Window") 
        self.setGeometry(100, 100, 400, 300) 
        self.centralwidget = QWidget() 
        self.setCentralWidget(self.centralwidget) 
        layout = QVBoxLayout() 
        self.textedit = QTextEdit() 
        layout.addWidget(self.textedit) 
        self.centralwidget.setLayout(layout) 
        # 添加垂直滚动条 
        scroll_bar = QScrollBar() 
        scroll_bar.setOrientation(Qt.Orientation.Vertical) 
        layout.addWidget(scroll_bar) 
def main(): 
    app = QApplication(sys.argv) 
    window = ScrollTextWindow() 
    window.show() 
    sys.exit(app.exec()) 
if __name__ == "__main__": 
    main() 
