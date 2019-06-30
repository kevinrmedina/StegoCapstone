from PyQt4 import QtGui
import os, sys
import subprocess

class Widget(QtGui.QWidget):

    def __init__(self):
        super(Widget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('StegSleuth File Browser')  

        pic = QtGui.QLabel(self)
        pic.setPixmap(QtGui.QPixmap("/root/StegSleuth.jpeg"))
        pic.show()
      
        btn = QtGui.QPushButton('Browse', self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.SingleBrowse)
        btn.move(350, 400) 
        self.show()

    def SingleBrowse(self):
        filePaths = QtGui.QFileDialog.getOpenFileNames(self, 
                                                   'StegSleuth File Browser',
                                                   "Home",
                                                  "(*.jpg *.png *.jpeg)")
     

def main():
    app = QtGui.QApplication(sys.argv)
    w = Widget()
    app.exec_()


if __name__ == '__main__':
    main()


