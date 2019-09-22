#!/usr/bin/env python3


import sys, os, subprocess
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from Hexdump3 import *
from hexPop import *

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

class PopUp(object):

	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(334, 186)
		self.label = QtWidgets.QLabel(Form)
		self.label.setGeometry(QtCore.QRect(50, 60, 241, 17))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(Form)
		self.label_2.setGeometry(QtCore.QRect(120, 80, 121, 16))
		self.label_2.setObjectName("label_2")
		self.noButton = QtWidgets.QPushButton(Form)
		self.noButton.setGeometry(QtCore.QRect(60, 130, 89, 25))
		self.noButton.setObjectName("noButton")
		self.yesButton = QtWidgets.QPushButton(Form)
		self.yesButton.setGeometry(QtCore.QRect(190, 130, 89, 25))
		self.yesButton.setObjectName("yesButton")

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

		self.noButton.clicked.connect(QtWidgets.qApp.quit)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.label.setText(_translate("Form", "Do you want to open the hexdump"))
		self.label_2.setText(_translate("Form", "in a text editor? "))
		self.noButton.setText(_translate("Form", "NO"))
		self.yesButton.setText(_translate("Form", "YES"))
						
if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())


