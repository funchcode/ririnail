from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class DailyCalendar(QTableWidget):
    def __init__(self):
        super().__init__()
        self.worker = ["원장님","Test"]
        self.partTime = ["9:00","9:30","10:00","10:30","11:00","11:30","12:00","12:30",
                         "13:00", "13:30","14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30",
                         "18:00", "18:30","19:00","19:30","20:00","20:30","21:00","21:30","22:00"]
        # self.wg = QWidget()
        # dailyCal = QTableWidget(self.wg)
        # dailyCal.setGeometry(10, 90, 1080, 150)
        # self.setCentralWidget(self.wg)

    def makeCalendar(self):
        options = DailyCalendar()
        wg = QWidget()
        dailyCal = QTableWidget(wg)
        dailyCal.setGeometry(10, 90, 800, 500)
        dailyCal.setColumnCount(len(options.worker))
        dailyCal.setHorizontalHeaderLabels(options.worker)
        dailyCal.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # Header Size 조정(균등하게)
        dailyCal.resizeColumnToContents(0)
        dailyCal.setRowCount(len(options.partTime))
        dailyCal.setVerticalHeaderLabels(options.partTime)
        #self.setCentralWidget(wg)
        return wg


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     exe = PayLayoutTest()
#     exe.show()
#     sys.exit(app.exec_())