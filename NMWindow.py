import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, \
    QTabWidget, QVBoxLayout, QPushButton, QFrame, QLabel, QLineEdit, QComboBox, QRadioButton
from PyQt5.QtCore import QRect

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
        pos1x = 20;
        pos1y = 20;
        pos1w = 60;
        pos1h = 60;


    def mkLayout(self):
        self.wg = QWidget()

        ''' 고객 정보 '''
        self.customFrame = QFrame(self.wg)
        self.customFrame.setGeometry(QRect(40, 20, 1120, 180))
        self.customFrame.setStyleSheet("QWidget{background-color:#ffffff};")
        customNoL = QLabel("고객 번호", self.customFrame)
        customNoL.setGeometry(20, 20, 60, 15)
        customNoE = QLineEdit(self.customFrame)
        customNoE.setGeometry(90, 20, 60, 15)
        customNoB = QPushButton("+", self.customFrame)
        customNoB.setGeometry(160, 20, 20, 15)

        customNameL = QLabel("고객 이름", self.customFrame)
        customNameL.setGeometry(20, 80, 60, 15)
        customNameE = QLineEdit(self.customFrame)
        customNameE.setGeometry(90, 80, 60, 15)

        customCellL = QLabel("연락처", self.customFrame)
        customCellL.setGeometry(20, 140, 60, 15)
        customCellE = QLineEdit(self.customFrame)
        customCellE.setGeometry(90, 140, 60, 15)

        customBirthL = QLabel("생년월일", self.customFrame)
        customBirthL.setGeometry(520, 20, 60, 15)
        customBirthE = QLineEdit(self.customFrame)
        customBirthE.setGeometry(590, 20, 60, 15)

        membershipL = QLabel("회원권", self.customFrame)
        membershipL.setGeometry(520, 80, 60, 15)
        membershipE = QLineEdit(self.customFrame)
        membershipE.setGeometry(590, 80, 60, 15)
        membershipB = QPushButton("+", self.customFrame)
        membershipB.setGeometry(660, 80, 20, 15)

        remainingAmountL = QLabel("남은 금액", self.customFrame)
        remainingAmountL.setGeometry(520, 140, 60, 15)
        remainingAmountE = QLineEdit(self.customFrame)
        remainingAmountE.setGeometry(590, 140, 60, 15)
        ''' end 고객 정보 '''

        ''' 결제 상세 정보 '''
        self.payDetailsFrame = QFrame(self.wg)
        self.payDetailsFrame.setGeometry(QRect(40, 210, 1120, 300))
        self.payDetailsFrame.setStyleSheet("QWidget{background-color:#aaaaaaaa};")

            # 결제 옵션 정보 #
        payOptionsFrame = QFrame(self.payDetailsFrame)
        payOptionsFrame.setGeometry(QRect(10,10,1100,100))
        payOptionsFrame.setFrameShadow(QFrame.Raised)
        nailKind = QLabel("종류", payOptionsFrame)
        nailKindCB = QComboBox(payOptionsFrame)
        nailKindCB.addItems(["시술종류"])
        nailKindCB.setGeometry(30,30,100,30)

        nailPrice = QLabel("가격", payOptionsFrame)
        nailPriceE = QLineEdit(payOptionsFrame)

        membershipUseYN = QLabel("회원권 사용", payOptionsFrame)
        membershipUseY = QRadioButton(payOptionsFrame)
        membershipUseY.setGeometry(80,80,10,10)
        membershipUseN = QRadioButton(payOptionsFrame)

        membershipCash = QLabel("회원권 금액", payOptionsFrame)

        discountPrice = QLabel("할인 금액", payOptionsFrame)

        payPrice = QLabel("결제 금액", payOptionsFrame)
            # end 결제 옵션 #
        ''' end 결제 상세 '''

        return self.wg



if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = NMWindow()
    exe.show()
    sys.exit(app.exec_())
