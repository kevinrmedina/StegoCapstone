#!/usr/bin/env python3


import sys, os, subprocess
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from Hexdump3 import *
from enum import Enum

class Ui_Form(object):
	
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.setFixedSize(750, 550)

		self.downloadButton = QtWidgets.QPushButton(Form)
		self.downloadButton.setGeometry(QtCore.QRect(60, 300, 171, 25))
		self.downloadButton.setObjectName("downloadButton")

		self.uploadButton = QtWidgets.QPushButton(Form)
		self.uploadButton.setGeometry(QtCore.QRect(90, 250, 111, 25))
		self.uploadButton.setObjectName("uploadButton")

		self.label = QtWidgets.QLabel(Form)
		self.label.setGeometry(QtCore.QRect(286, 26, 261, 361))
		self.label.setFrameShape(QtWidgets.QFrame.Box)
		self.label.setObjectName("label")

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)
		
		self.uploadButton.clicked.connect(self.openFile)
		self.downloadButton.clicked.connect(self.saveFile)
	
	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.downloadButton.setText(_translate("Form", " Download Hexdump"))
		self.uploadButton.setText(_translate("Form", "Upload FIle"))
		
	def openFile(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		self.fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", " ", "All Files (*)", options = options)
		if self.fileName:
			image = QPixmap(self.fileName)
			self.label.setPixmap(image)
			self.label.resize(image.width(), image.height())
	
	def saveFile(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName2, _ = QFileDialog.getSaveFileName(None, "QFileDialog.getSaveFileName()", " ", "All Files (*)", options = options)
		if fileName2:
			file = self.fileName
			subprocess.call(["./Hexdump3.py", file, fileName2])

						
if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())


