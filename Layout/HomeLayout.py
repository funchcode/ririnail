from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from tools.DailyCalendar import *

class PayLayoutTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1200, 700)
        self.setWindowTitle("HomeLayout")

        # dailyCal = QTableWidget(self.wg)
        # dailyCal.setGeometry(10, 90, 1080, 150)
        # DailyCalendar.makeCalendar(self)
        dailyCal = DailyCalendar.makeCalendar(self)
        self.setCentralWidget(dailyCal)


if __name__ == "__main__":
    QApplication.setStyle('Windows')
    app = QApplication(sys.argv)
    exe = PayLayoutTest()
    exe.show()
    sys.exit(app.exec_())