from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from tools.DailyCalendar import *

class ReservationLayout(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1200, 700)
        self.setWindowTitle("HomeLayout")

        # dailyCal = QTableWidget(self.wg)
        # dailyCal.setGeometry(10, 90, 1080, 150)
        # DailyCalendar.makeCalendar(self)
        '''
            DailyCalendar 시작
        '''
        dailyCal = DailyCalendar.makeCalendar(self)
        self.setCentralWidget(dailyCal)
        '''
            end DailyCalendar
        '''

        '''
            Calendar 시작
        '''
        calendar = QCalendarWidget(self)
        calendar.setGeometry(680, 90, 300, 200)
        '''
            end Calendar
        '''

        '''
        '''
        reservationSheet = QTableWidget(self)
        reservationSheet.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        reservationSheet.setGeometry(600, 320, 480, 260)
        reservationHeader = ["예약시간","이름","시술종류","연락처","담당자"]
        reservationSheet.setColumnCount(len(reservationHeader))
        reservationSheet.setHorizontalHeaderLabels(reservationHeader)
        '''
        
        '''

# if __name__ == "__main__":
#     QApplication.setStyle('Windows')
#     app = QApplication(sys.argv)
#     exe = HomeLayout()
#     exe.show()
#     sys.exit(app.exec_())