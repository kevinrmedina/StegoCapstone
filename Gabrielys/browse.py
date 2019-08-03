#!/usr/bin/env python3

import sys, os, subprocess
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from stegScript import *
from PIL import Image

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
			# Print the image path
			print(fileName)
	
			# It is a test to confirm the operation of the open button.
			image = Image.open(fileName)
			image.show()

			#carrier = fileName
			#subprocess.Popen(['./stegScript.py', '-e', '-f', carrier], shell = True)
			

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())
