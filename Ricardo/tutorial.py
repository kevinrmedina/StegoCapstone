import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDesktopWidget, QLabel



# Initial Page
class Example(QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
    
    def onTopButtonClicked(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Second Page'))
        layout.addWidget(QLabel('Random Label'))
        self.setLayout(layout)
        self.show()

    def initUI(self):               
        
        self.resize(500, 500)
        self.center()
        
        self.setWindowTitle('Center')  
        
        layout = QVBoxLayout() 
        secondPageButton = QPushButton('Navigate To Page')
        layout.addWidget(secondPageButton)
        secondPageButton.clicked.connect(self.onTopButtonClicked)
        layout.addWidget(QPushButton('Top')) 
        layout.addWidget(QPushButton('Bottom')) 
        self.setLayout(layout)
        self.show()
        
    def center(self):
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    

        
        
def main():
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()  