#!usr/bin/env python3

import sys, os, subprocess
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
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setGeometry(QtCore.QRect(600, 470, 89, 25))
        self.closeButton.setObjectName("closeButton")
        self.carrierScrollArea = QtWidgets.QScrollArea(Form)
        self.carrierScrollArea.setGeometry(QtCore.QRect(360, 10, 370, 450))
        self.carrierScrollArea.setWidgetResizable(True)
        self.carrierScrollArea.setObjectName("carrierScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 368, 448))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.carrierScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
	
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.downloadButton.setText(_translate("Form", " Download Hexdump"))
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
        if self.fileName:
            image = QPixmap(self.fileName)
            self.label.setPixmap(image)
            self.label.resize(image.width(), image.height())
	
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

