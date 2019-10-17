#!/usr/bin/env python3

import sys, os, subprocess, re
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMessageBox, QAction
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from Hexdump3 import *
from enum import Enum

class Hex_GUI(object):
	
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.setFixedSize(750, 550)

		self.downloadButton = QtWidgets.QPushButton(Form)
		self.downloadButton.setGeometry(QtCore.QRect(60, 300, 171, 25))
		self.downloadButton.setObjectName("downloadButton")

		self.uploadButton = QtWidgets.QPushButton(Form)
		self.uploadButton.setGeometry(QtCore.QRect(90, 250, 111, 25))
		self.uploadButton.setObjectName("uploadButton")

		self.scrollArea = QtWidgets.QScrollArea(Form)
		self.scrollArea.setGeometry(QtCore.QRect(280, 20, 411, 411))
		#self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName("scrollArea")
		self.scrollAreaWidgetContents = QtWidgets.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 409, 409))
		self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

		self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
		self.label.setGeometry(QtCore.QRect(26, 16, 361, 371))
		#self.label.setFrameShape(QtWidgets.QFrame.Box)
		self.label.setObjectName("label")
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		

		self.closeButton = QtWidgets.QPushButton(Form)
		self.closeButton.setGeometry(QtCore.QRect(600, 470, 89, 25))
		self.closeButton.setObjectName("closeButton")

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

				
		self.uploadButton.clicked.connect(self.openFile)
		self.downloadButton.clicked.connect(self.saveFile)
		self.downloadButton.clicked.connect(self.showPop)
		self.closeButton.clicked.connect(QApplication.quit)
	
	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.downloadButton.setText(_translate("Form", " Generate Hexdump"))
		self.uploadButton.setText(_translate("Form", "Upload File"))
		self.closeButton.setText(_translate("Form", "Close"))

	def showPop(self):
		msgBox = QMessageBox()
		msgBox.setWindowTitle("Open Window")
		msgBox.setText("Do you want to open the hexdump in a text editor?   ")
		msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		
		returnValue = msgBox.exec_()
		if returnValue == QMessageBox.Yes:
			subprocess.Popen(['xdg-open', self.fileName2])
			
	def openFile(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		self.fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", " ", "All Files (*)", options = options)
		image = QPixmap(self.fileName)
		fileExtension = re.sub(r'.*\.', '', self.fileName)
		if fileExtension == 'png' or fileExtension == 'jpg' or fileExtension == 'jpeg' or fileExtension == 'bmp' or fileExtension == 'gif': 
			self.label.setPixmap(image)
			#self.label.resize(image.width(), image.height())
		else:
			self.label.setText(self.fileName)
			
	def saveFile(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		self.fileName2, _ = QFileDialog.getSaveFileName(None, "QFileDialog.getSaveFileName()", " ", "All Files (*)", options = options)
		if self.fileName2:
			file = self.fileName
			subprocess.call(["./Hexdump3.py", file, self.fileName2])
						
if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = Hex_GUI()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())


