#!/usr/bin/env python

import sys, os, subprocess
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from stegScript import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("StegSleuth")
        Form.resize(800, 800)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("Browse")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

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
    	fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","*.png", options=options)
    	if fileName:
        	print(fileName)
		subprocess.popen(['./stegScript.py', '-e', '-f', carrier, payload], shell = True)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
