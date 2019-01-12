import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class TabLayout(QMainWindow):
    def __init__(self):
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
        payMenu.triggered.connect(self.addTabs)
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
        tab1 = QWidget()
        self.tabs.resize(300, 200)

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

    def addTabs(self):
        tab2 = QWidget()
        tab2.layout = QVBoxLayout()
        QLineEdit(tab2)
        tab2.setLayout(tab2.layout)
        self.tabs.addTab(tab2, "TEST")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = TabLayout()
    exe.show()
    sys.exit(app.exec_())
