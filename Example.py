import sys
from PyQt5.QtWidgets import *

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 450)
        self.setWindowTitle('Sample Title')



        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        menubar.addMenu('매출관리')
        menubar.addMenu('예약관리')
        menubar.addMenu('마케팅관리')
        menubar.addMenu('기초등록')
        menubar.addMenu('고객관리')
        menubar.addMenu('직원관리')
        menubar.addMenu('매장관리')

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())