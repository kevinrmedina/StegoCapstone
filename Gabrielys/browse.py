#!/usr/bin/env python3

import sys, os
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from stegScript import *

class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName("StegSleuth")
		Form.resize(320,200)
		self.pushButton = QtWidgets.QPushButton(Form)
		self. pushButton.setObjectName("Browse")
		self.pushButton.move(115,80)
		
		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)
		
		self.pushButton.clicked.connect(self.openFile)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("StegSleuth", "StegSleuth"))
		self.pushButton.setText(_translate("StegSleuth", "Browse"))

	def openFile(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "*.png", options = options)
				
		if fileName:
			print(fileName)
			#carrier = fileName
			#subprocess.popen(["stegScript.py", "-e", carrier])

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())
