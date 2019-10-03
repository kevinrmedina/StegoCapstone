# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EncodeFile.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 550)
        self.selectPayload = QtWidgets.QPushButton(Form)
        self.selectPayload.setGeometry(QtCore.QRect(10, 450, 121, 51))
        self.selectPayload.setObjectName("selectPayload")
        self.previousButton = QtWidgets.QPushButton(Form)
        self.previousButton.setGeometry(QtCore.QRect(430, 450, 113, 51))
        self.previousButton.setObjectName("previousButton")
        self.nextButton = QtWidgets.QPushButton(Form)
        self.nextButton.setGeometry(QtCore.QRect(560, 450, 113, 51))
        self.nextButton.setObjectName("nextButton")
        self.payloadScrollArea = QtWidgets.QScrollArea(Form)
        self.payloadScrollArea.setGeometry(QtCore.QRect(10, 10, 349, 421))
        self.payloadScrollArea.setWidgetResizable(True)
        self.payloadScrollArea.setObjectName("payloadScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 347, 419))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.payloadLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.payloadLabel.setObjectName("payloadLabel")
        self.gridLayout_3.addWidget(self.payloadLabel, 0, 0, 1, 1)
        self.payloadScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.carrierScrollArea = QtWidgets.QScrollArea(Form)
        self.carrierScrollArea.setGeometry(QtCore.QRect(390, 10, 349, 421))
        self.carrierScrollArea.setWidgetResizable(True)
        self.carrierScrollArea.setObjectName("carrierScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 347, 419))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.carrierLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.carrierLabel.setObjectName("carrierLabel")
        self.gridLayout_4.addWidget(self.carrierLabel, 0, 0, 1, 1)
        self.carrierScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.selectPayload.setText(_translate("Form", "Select Payload"))
        self.previousButton.setText(_translate("Form", "Previous"))
        self.nextButton.setText(_translate("Form", "Next"))
        self.payloadLabel.setText(_translate("Form", "<html><head/><body><p><img src=\":/translation_images/hieroglyphics.jpg\"/></p></body></html>"))
        self.carrierLabel.setText(_translate("Form", "<html><head/><body><p><img src=\":/translation_images/hieroglyphics.jpg\"/></p></body></html>"))

