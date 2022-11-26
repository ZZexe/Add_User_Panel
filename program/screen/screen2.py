import sys
from PyQt5.QtWidgets import *


def Window():

    app = QApplication(sys.argv)

    win = QMainWindow()

    win.setWindowTitle("Hello PyQt5")

    win.setGeometry(100, 100, 600, 600)

    hello = QLabel(win)
    hello.setGeometry(50,50,200,200)

    button1 = QPushButton("Click", win)
    button1.setGeometry(200,200,100,50)

    hello.setText("Hellooooo")

    win.show()

    sys.exit(app.exec_())


Window()