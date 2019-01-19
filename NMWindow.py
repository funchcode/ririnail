import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, \
    QTabWidget, QVBoxLayout, QPushButton, QFrame, QLabel, QLineEdit, QComboBox, QRadioButton, \
    QTableWidget, QHeaderView
from PyQt5.QtCore import QRect
from Layout.PayLayout import *

class NMWindow(QMainWindow):
    def __init__(self):
        self.tabWidgets = ["HOME"]
        super(NMWindow, self).__init__()
        self.setGeometry(100, 100, 1200, 700)
        self.setWindowTitle("RIRI NAIL SALON")

        '''
        Menubar Zone
        '''
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        saleBar = menubar.addMenu("판매관리")
        payMenu = QAction("결제화면", self)
        payMenu.triggered.connect(lambda: self.tabManager(payMenu.text()))
        dailyClosingMenu = QAction("일마감현황", self)

        salesDetailsMenu = QAction("매출상세", self)
        productReceiptMenu = QAction("제품입고", self)
        productDetailsMenu = QAction("제품상세", self)
        saleBar.addAction(payMenu)
        saleBar.addAction(dailyClosingMenu)
        saleBar.addAction(salesDetailsMenu)
        saleBar.addAction(productReceiptMenu)
        saleBar.addAction(productDetailsMenu)

        reservationBar = menubar.addMenu("예약관리")
        reservationMenu = QAction("예약현황", self)
        reservationBar.addAction(reservationMenu)

        marketingBar = menubar.addMenu("마케팅관리")
        sendTextMenu = QAction("문자발송", self)
        marketingBar.addAction(sendTextMenu)

        settingBar = menubar.addMenu("기초등록")
        serviceMenu = QAction("서비스메뉴등록", self)
        settingBar.addAction(serviceMenu)

        customerBar = menubar.addMenu("고객관리")
        customEnrollMenu = QAction("고객등록", self)
        customInquiryMenu = QAction("고객조회", self)
        customDetailsMenu = QAction("고객상세", self)
        customerBar.addAction(customEnrollMenu)
        customerBar.addAction(customInquiryMenu)
        customerBar.addAction(customDetailsMenu)

        employeeBar = menubar.addMenu("직원관리")
        employSalesMenu = QAction("직원매출관리", self)
        employeeBar.addAction(employSalesMenu)

        storeBar = menubar.addMenu("매장관리")
        incomeMenu = QAction("손익계산", self)
        storeBar.addAction(incomeMenu)
        ''' 
        end Menubar
        '''

        '''
        QTabWidget Zone
        '''
        tabWidget = QWidget()
        tabWidget.layout = QVBoxLayout(tabWidget)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        tab1 = QWidget()
        self.tabs.resize(300, 200)

        self.tabs.addTab(tab1, "HOME")
        self.tabs.tabBar().setTabButton(0, QTabBar.RightSide, None) # 첫 번째 탭은 닫기 버튼 제거
        tab1.layout = QVBoxLayout()
        pushButton = QPushButton("Test Btn")
        tab1.layout.addWidget(pushButton)
        tab1.setLayout(tab1.layout)

        tabWidget.layout.addWidget(self.tabs)
        tabWidget.setLayout(tabWidget.layout)

        self.setCentralWidget(tabWidget)
        '''
        end QTabWidget
        '''

    def tabManager(self, tabName): # 탭이 삭제되었을 때 Index 처리 ({} -> [])
        if tabName in self.tabWidgets:
            self.tabs.setCurrentIndex(self.tabWidgets.index(tabName))
        else:
            # tab2 = QWidget()
            # tab2.layout = QVBoxLayout()
            # QLineEdit(tab2)
            # tab2.setLayout(tab2.layout)
            #self.tabs.addTab(tab2, tabName)
            if tabName == "결제화면":
                newTab = PayLayout()
            self.tabs.addTab(newTab, tabName)
            self.tabs.setCurrentIndex(self.tabs.count()-1)          # setCurrentIndex로 보여주는 탭을 변경
            self.tabWidgets.append(tabName)                         # 리스트로 관리

if __name__ == "__main__":
    QApplication.setStyle('Windows')
    app = QApplication(sys.argv)
    exe = NMWindow()
    exe.show()
    sys.exit(app.exec_())
