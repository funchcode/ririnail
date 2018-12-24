from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

class TestApp(QWidget):
    def __init__(self):
        super.__init__()
        self.initUI(self)

    def initUI(self):
        self.showNormal()