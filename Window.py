import sys
from PyQt5.QtWidgets import *


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # 탭 초기화 화면
        self.tabs = QTabWidget()
        self.homeTab = QWidget()
        self.tabs.resize(300,200)

        # 탭 추가
        self.tabs.addTab(self.homeTab, "HOME")

        # "HOME" 탭 생성
        self.homeTab.layout = QVBoxLayout(self)
        self.pushButton = QPushButton("QT5")
        self.homeTab.layout.addWidget(self.pushButton)
        self.homeTab.setLayout(self.homeTab.layout)

        # 위젯에 탭 추가
        self.layout.addWidget(self.homeTab)
        self.setLayout(self.layout)



class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 menu'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.defaultMenuBar()

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)


    def defaultMenuBar(self):
        # Top Menu Bar 선언
        mainMenu = self.menuBar()

        # Mac일 때(?)
        mainMenu.setNativeMenuBar(False)
        salesMenu = mainMenu.addMenu('판매관리')
        reservationMenu = mainMenu.addMenu('예약관리')
        marketingMenu = mainMenu.addMenu('마케팅관리')
        baseRegistMenu = mainMenu.addMenu('기초등록')
        customerMenu = mainMenu.addMenu('고객관리')
        staffMenu = mainMenu.addMenu('직원관리')
        storeMenu = mainMenu.addMenu('매장관리')

        salesMenu.addAction("결제화면")
        salesMenu.addAction("일마감현황")
        salesMenu.addAction("매출상세")
        salesMenu.addAction("제품입고")
        salesMenu.addAction("제품상세")

        reservationMenu.addAction("예약현황")

        marketingMenu.addAction("문자발송")

        baseRegistMenu.addAction("서비스메뉴 등록")

        customerMenu.addAction("고객등록")
        customerMenu.addAction("고객조회")
        customerMenu.addAction("고객상세")

        staffMenu.addAction("직원매출관리")

        storeMenu.addAction("손익계산")




# 메인함수가 없다.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())