import sys
from PyQt5.QtWidgets import *

class TabTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 menu'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    def setTabLayout(self, tab):
        self.setCentralWidget(tab)

class Tabs(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)

        self.tabArea = QTabWidget()
        self.homeTab = QWidget()
        # self.tabArea.resize(30, 100)

        self.tabArea.addTab(self.homeTab, "home")

        self.homeTab.layout = QVBoxLayout(self)
        self.pushButton = QPushButton("btn")
        self.homeTab.layout.addWidget(self.pushButton)
        self.homeTab.setLayout(self.homeTab.layout)

        self.layout.addWidget(self.tabArea)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TabTest()
    ex.setCentralWidget(Tabs(ex))
    ex.show()
    sys.exit(app.exec_())
