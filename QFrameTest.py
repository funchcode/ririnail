import sys
from PyQt5.QtWidgets import *


class QFrameTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1200, 700)
        self.setWindowTitle("QFrameTest")

        wg = QWidget(self)
        btn = QPushButton(QFrame(wg))

        self.setCentralWidget(wg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = QFrameTest()
    exe.show()
    sys.exit(app.exec_())
