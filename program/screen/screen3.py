import sys
from PyQt5.QtWidgets import *


class Win(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()



    def initUI(self):
        
        self.setGeometry(100,100,600,400)
        self.setWindowTitle("Hello")
        a = self.label = QLabel("Hi", self)
        a.setGeometry(50,50,300,200)







if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = Win()

    sys.exit(app.exec_())