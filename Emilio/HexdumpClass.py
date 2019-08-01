import sys
import Hexdump
from PyQt5 import QtWidgets, uic, QtGui

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() 
        uic.loadUi('Hexdump.ui', self) 
	self.show()

    def HexdumpOutput(self):
	self.Hexdump.append(parser.usage(str(text) + ' '))

app = QtWidgets.QApplication(sys.argv) 
window = Ui() 
app.exec_()
