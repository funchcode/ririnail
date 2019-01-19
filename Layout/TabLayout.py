import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import Layout.PayLayout


class TabLayout(QMainWindow):
    def __init__(self):
        self.tabWidgets = ["HOME"]
        super(TabLayout, self).__init__()
        self.setGeometry(100, 100, 1200, 700)
        self.setWindowTitle("RIRI NAIL SALON")

        '''
        Menubar Zone
        '''
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        saleBar = menubar.addMenu("판매관리")
        payMenu = QAction("결제화면", self)
        payMenu.triggered.connect(lambda: self.addTabs(payMenu.text()))    # lambda로 self와 파라미터를 보낼 수 있다.
        dailyClosingMenu = QAction("일마감현황", self)
        salesDetailsMenu = QAction("매출상세", self)
        productReceiptMenu = QAction("제품입고", self)
        productDetailsMenu = QAction("제품상세", self)
        saleBar.addAction(payMenu)
        saleBar.addAction(dailyClosingMenu)
        saleBar.addAction(salesDetailsMenu)
        saleBar.addAction(productReceiptMenu)
        saleBar.addAction(productDetailsMenu)
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
        print(self.tabs.tabsClosable())                                 # 버전 5부터에서는 Mac에서 확인할 수 없다.
        # self.tabs.tabBar().setStyleSheet("QTabBar::close-button{background-image:url(\"../image/xicon.png\")}") # Mac에서 확인할 수 없어서 커스텀마이징
        self.tabs.setStyleSheet("QTabWidget::tab-bar{alignment:left}")
        tab1 = QWidget()
        self.tabs.resize(300, 200)
        self.tabs.setContentsMargins(9,9,9,9)

        self.tabs.addTab(tab1, "HOME")
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


    def addTabs(self, tabName): # 탭이 삭제되었을 때 Index 처리 ({} -> [])
        if tabName in self.tabWidgets:
            self.tabs.setCurrentIndex(self.tabWidgets.index(tabName))
        else:
            tab2 = QWidget()
            tab2.layout = QVBoxLayout()
            QLineEdit(tab2)
            tab2.setLayout(tab2.layout)
            customTab = Layout.PayLayout.PayLayoutTest()
            #self.tabs.addTab(tab2, tabName)                         #
            self.tabs.addTab(customTab, tabName)
            self.tabs.setCurrentIndex(self.tabs.count()-1)          # setCurrentIndex로 보여주는 탭을 변경
            self.tabWidgets.append(tabName)                         # 리스트로 관리



if __name__ == "__main__":
    QApplication.setStyle('Windows') # ['Windows', 'Fusion', 'Macintosh'] 스타일이 존재함.
    app = QApplication(sys.argv)
    exe = TabLayout()
    exe.show()
    sys.exit(app.exec_())
