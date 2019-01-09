import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QWidget, QAction, \
    QTabWidget, QVBoxLayout, QPushButton, QFrame

class NMWindow(QMainWindow):
    def __init__(self):
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
        payMenu.triggered.connect(self.changeLayout)
        dailyClosingMenu = QAction("일마감현황", self)
        paylayout = PayLayout()
        dailyClosingMenu.triggered.connect(self.changeLayout)

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
        '''
        end QTabWidget
        '''


    def changeLayout(self):
        #changeButton = QPushButton("changed!!")
        changeButton = PayLayout().mkLayout()
        self.setCentralWidget(changeButton)

class PayLayout(QWidget):
    def __init__(self):
        super(PayLayout, self).__init__()

    def mkLayout(self):
        self.wg = QWidget()
        self.btn = QPushButton("다른 클래스",QFrame(self.wg))
        return self.wg




if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = NMWindow()
    exe.show()
    sys.exit(app.exec_())
