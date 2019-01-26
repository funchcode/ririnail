from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from tools.DailyCalendar import *


class WorkClosed(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1200, 700)
        self.setWindowTitle("HomeLayout")
        headerList = ["시간", "고객", "구분", "상세", "현금", "카드", "통장", "외상", "정액", "담당자"]
        '''
            조건
        '''
        condition = QFrame(self)
        condition.setGeometry(50, 40, 1100, 100)
        condition.setStyleSheet("QWidget{background-color:#ffffff};")
        dateL = QLabel("날짜", condition)
        dateL.setGeometry(10, 40, 100, 15)
        startDate = QDateTimeEdit(condition)
        startDate.setGeometry(100, 40, 150, 20)
        endDate = QDateTimeEdit(condition)
        endDate.setGeometry(300, 40, 150, 20)

        typeL = QLabel("구분", condition)
        typeL.setGeometry(600, 40, 100, 15)
        typeBox1 = QComboBox(condition)
        typeBox1.setGeometry(700, 40, 50, 20)
        typeBox2 = QComboBox(condition)
        typeBox2.setGeometry(750, 40, 50, 20)

        workerL = QLabel("대상", condition)
        workerL.setGeometry(900, 40, 50, 15)
        workerBox = QComboBox(condition)
        workerBox.setGeometry(950, 40, 50, 20)

        searchBtn = QPushButton("검색", condition)
        searchBtn.setGeometry(1000, 40, 50, 20)
        '''
            end 조건
        '''

        '''
            마감리스트
        '''
        workCloseListWg = QFrame(self)
        workCloseListWg.setGeometry(50, 160, 700, 400)
        workCloseListWg.setStyleSheet("QWidget{background-color:#ffffff};")

        workCloseList = QTableWidget(workCloseListWg)
        workCloseList.setGeometry(5, 5, 690, 390)
        workCloseList.setColumnCount(10)
        workCloseList.setHorizontalHeaderLabels(headerList)
        '''
            end 마감리스트
        '''

        '''
            총 합산(Dummy Data)
        '''
        totalWg = QFrame(self)
        totalWg.setGeometry(800, 160, 350, 400)
        totalWg.setStyleSheet("QWidget{background-color:#ffffff};")
        totalLayout = QFormLayout(totalWg)
        totalLayout.addRow("날짜:     ", QLabel("2019-01-01 ~ 2019-01-01"))
        totalLayout.addRow("구분1:    ", QLabel("1,000,000,000"))
        totalLayout.addRow("구분2:    ", QLabel("1,000,000,000"))
        totalLayout.addRow("구분3:    ", QLabel("1,000,000,000"))
        totalLayout.addRow("현금:     ", QLabel("1,000,000,000"))
        totalLayout.addRow("카드:     ", QLabel("1,000,000,000"))
        totalLayout.addRow("통장:     ", QLabel("1,000,000,000"))
        totalLayout.addRow("외상:     ", QLabel("1,000,000,000"))
        totalLayout.addRow("정액:     ", QLabel("1,000,000,000"))
        '''
            end 총 합산
        '''

# if __name__ == "__main__":
#     QApplication.setStyle('Windows')
#     app = QApplication(sys.argv)
#     exe = WorkClosed()
#     exe.show()
#     sys.exit(app.exec_())