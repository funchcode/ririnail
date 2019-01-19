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
                newTab = PayLayoutTest()
            self.tabs.addTab(newTab, tabName)
            self.tabs.setCurrentIndex(self.tabs.count()-1)          # setCurrentIndex로 보여주는 탭을 변경
            self.tabWidgets.append(tabName)                         # 리스트로 관리


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
        self.payDetailsFrame.setGeometry(QRect(40, 210, 1120, 400))
        self.payDetailsFrame.setStyleSheet("QWidget{background-color:#aaaaaaaa};")

        # 결제 옵션 정보 #
        payOptionsFrame = QFrame(self.payDetailsFrame)
        payOptionsFrame.setGeometry(QRect(10, 10, 1100, 250))
        payOptionsFrame.setFrameShadow(QFrame.Raised)
        nailKind = QLabel("종류", payOptionsFrame)
        nailKind.setGeometry(30, 15, 100, 20)
        nailKindCB = QComboBox(payOptionsFrame)
        nailKindCB.addItems(["시술종류"])
        nailKindCB.setGeometry(120, 10, 100, 30)

        nailPrice = QLabel("가격", payOptionsFrame)
        nailPrice.setGeometry(30, 60, 100, 20)
        nailPriceE = QLineEdit(payOptionsFrame)
        nailPriceE.setGeometry(120, 60, 100, 20)

        membershipUseYN = QLabel("회원권 사용", payOptionsFrame)
        membershipUseYN.setGeometry(350, 15, 80, 20)
        membershipUseY = QRadioButton("사용", payOptionsFrame)
        membershipUseY.setGeometry(450, 15, 50, 17)
        membershipUseN = QRadioButton("미사용", payOptionsFrame)
        membershipUseN.setGeometry(510, 15, 60, 17)

        membershipCash = QLabel("회원권 금액", payOptionsFrame)
        membershipCash.setGeometry(350, 60, 100, 20)
        membershipCashE = QLineEdit(payOptionsFrame)
        membershipCashE.setGeometry(450, 60, 100, 20)

        discountPrice = QLabel("할인 금액", payOptionsFrame)
        discountPrice.setGeometry(650, 15, 100, 20)
        discountPriceE = QLineEdit(payOptionsFrame)
        discountPriceE.setGeometry(760, 15, 100, 20)

        payPrice = QLabel("결제 금액", payOptionsFrame)
        payPrice.setGeometry(650, 60, 100, 20)
        payPriceE = QLineEdit(payOptionsFrame)
        payPriceE.setGeometry(760, 60, 100, 20)
        # end 결제 옵션 #

        # 결제 목록 Table #
        column_headers = ["종류","가격","담당자","회원권 사용","회원권 금액","할인 금액","결제 금액"]

        payTable = QTableWidget(payOptionsFrame)
        payTable.setGeometry(10, 90, 1080, 150)
        payTable.setColumnCount(7)
        payTable.setHorizontalHeaderLabels(column_headers)
        payTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # end 결제 목록 #
        ''' end 결제 상세 '''

        ''' 결제 합산 totalPay '''
        payDate = QLabel("결제 날짜", self.payDetailsFrame)
        payDate.setGeometry(10, 280, 100, 20)
        payYear = QLineEdit(self.payDetailsFrame)
        payYear.setGeometry(120, 280, 100, 20)
        payMonth = QLineEdit(self.payDetailsFrame)
        payMonth.setGeometry(230, 280, 100, 20)
        payDay = QLineEdit(self.payDetailsFrame)
        payDay.setGeometry(340, 280, 100, 20)

        payOption = QLabel("결제 수단", self.payDetailsFrame)
        payOption.setGeometry(10, 320, 100, 20)
        payCash = QRadioButton("현금", self.payDetailsFrame)
        payCash.setGeometry(120, 320, 50, 17)
        payCard = QRadioButton("카드", self.payDetailsFrame)
        payCard.setGeometry(230, 320, 60, 17)

        memo = QLabel("메모", self.payDetailsFrame)
        memo.setGeometry(10, 360, 100, 20)
        memoE = QLineEdit(self.payDetailsFrame)
        memoE.setGeometry(120, 360, 200, 20)

        costPrice = QLabel("원 금액", self.payDetailsFrame)
        costPrice.setGeometry(600, 280, 100, 20)
        costPriceE = QLineEdit(self.payDetailsFrame)
        costPriceE.setGeometry(720, 280, 100, 20)

        dCostPrice = QLabel("할인 금액", self.payDetailsFrame)
        dCostPrice.setGeometry(600, 320, 100, 20)
        dCostPriceE = QLineEdit(self.payDetailsFrame)
        dCostPriceE.setGeometry(720, 320, 100, 20)

        tCostPrice = QLabel("총 금액", self.payDetailsFrame)
        tCostPrice.setGeometry(600, 360, 100, 20)
        tCostPriceE = QLineEdit(self.payDetailsFrame)
        tCostPriceE.setGeometry(720, 360, 100, 20)
        ''' end 결제 합산 '''

        return self.wg



if __name__ == "__main__":
    QApplication.setStyle('Windows')
    app = QApplication(sys.argv)
    exe = NMWindow()
    exe.show()
    sys.exit(app.exec_())
