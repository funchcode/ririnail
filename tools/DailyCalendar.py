from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class DailyCalendar(QTableWidget):
    def __init__(self):
        super().__init__()
        # self.wg = QWidget()
        # dailyCal = QTableWidget(self.wg)
        # dailyCal.setGeometry(10, 90, 1080, 150)
        # self.setCentralWidget(self.wg)

    def makeCalendar(self):
        wg = QWidget()
        dailyCal = QTableWidget(wg)
        dailyCal.setGeometry(10, 90, 1080, 150)
        #self.setCentralWidget(wg)
        return wg


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     exe = PayLayoutTest()
#     exe.show()
#     sys.exit(app.exec_())