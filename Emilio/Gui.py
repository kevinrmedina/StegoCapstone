import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class Window (QMainWindow):
	def __init__(self):
		QMainWindow._init_(self)
		uic.loadUi("mainwindow.ui",self)

app= QApplication(sys.argv)
_window = Window()
_window.show()
app.exec_()
