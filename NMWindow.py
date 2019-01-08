import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QWidget, QAction, QTabWidget, QVBoxLayout, QPushButton

class NMWindow(QMainWindow):
    def __init__(self):
        super(NMWindow, self).__init__()
        self.setGeometry(100, 100, 801, 461)
        self.setWindowTitle("RIRI NAIL SALON")

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        saleMenu = menubar.addMenu("판매관리")
        saleMenu.addAction("결제화면")
        saleMenu.addAction("일마감현황")
        saleMenu.addAction("매출상세")
        saleMenu.addAction("제품입고")
        saleMenu.addAction("제품상세")
        reservationMenu = menubar.addMenu("예약관리")
        reservationMenu.addAction("예약현황")
        marketingMenu = menubar.addMenu("마케팅관리")
        marketingMenu.addAction("문자발송")
        settingMenu = menubar.addMenu("기초등록")
        settingMenu.addAction("서비스메뉴등록")
        customerMenu = menubar.addMenu("고객관리")
        customerMenu.addAction("고객등록")
        customerMenu.addAction("고객조회")
        customerMenu.addAction("고객상세")
        employeeMenu = menubar.addMenu("직원관리")
        employeeMenu.addAction("직원매출관리")
        storeMenu = menubar.addMenu("매장관리")
        storeMenu.addAction("손익계산")

        tabWidget = QWidget()
        tabWidget.layout = QVBoxLayout(tabWidget)

        tabs = QTabWidget()
        tab1 = QWidget()
        tabs.resize(300, 200)

        tabs.addTab(tab1, "HOME")
        tab1.layout = QVBoxLayout()
        pushButton = QPushButton("Test Btn")
        tab1.layout.addWidget(pushButton)
        tab1.setLayout(tab1.layout)

        tabWidget.layout.addWidget(tabs)
        tabWidget.setLayout(tabWidget.layout)

        self.setCentralWidget(tabWidget)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = NMWindow()
    exe.show()
    sys.exit(app.exec_())
