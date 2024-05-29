from PyQt6 import QtWidgets, QtGui, QtCore
import sys

class TabDemo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # 創建 QTabWidget
        self.tabs = QtWidgets.QTabWidget()

        # 創建兩個頁籤
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()

        # 將頁籤加入 QTabWidget
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")

        # 設置 Tab1 的布局
        self.tab1.layout = QtWidgets.QVBoxLayout()
        self.tab1.label = QtWidgets.QLabel("This is Tab 1")
        self.tab1.layout.addWidget(self.tab1.label)
        self.tab1.setLayout(self.tab1.layout)

        # 設置 Tab2 的布局
        self.tab2.layout = QtWidgets.QVBoxLayout()
        self.tab2.label = QtWidgets.QLabel("This is Tab 2")
        self.tab2.layout.addWidget(self.tab2.label)
        self.tab2.setLayout(self.tab2.layout)

        # 設置主布局
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        self.setWindowTitle("QTabWidget Example")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    demo = TabDemo()
    demo.show()
    sys.exit(app.exec())