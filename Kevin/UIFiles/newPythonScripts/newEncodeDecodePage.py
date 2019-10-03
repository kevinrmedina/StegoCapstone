# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EncodeDecodePage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 550)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 120, 111, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.decodeRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.decodeRadioButton.setObjectName("decodeRadioButton")
        self.verticalLayout.addWidget(self.decodeRadioButton)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(450, 460, 221, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previousButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousButton.sizePolicy().hasHeightForWidth())
        self.previousButton.setSizePolicy(sizePolicy)
        self.previousButton.setMinimumSize(QtCore.QSize(0, 50))
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout.addWidget(self.previousButton)
        self.nextButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.nextButton.setMinimumSize(QtCore.QSize(0, 50))
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout.addWidget(self.nextButton)
        self.carrierScrollArea = QtWidgets.QScrollArea(Form)
        self.carrierScrollArea.setGeometry(QtCore.QRect(370, 10, 370, 450))
        self.carrierScrollArea.setWidgetResizable(True)
        self.carrierScrollArea.setObjectName("carrierScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 368, 448))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.carrierLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.carrierLabel.setObjectName("carrierLabel")
        self.gridLayout_3.addWidget(self.carrierLabel, 0, 0, 1, 1)
        self.carrierScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioButton_2.setText(_translate("Form", "Encode"))
        self.decodeRadioButton.setText(_translate("Form", "Decode"))
        self.previousButton.setText(_translate("Form", "Prev"))
        self.nextButton.setText(_translate("Form", "Next"))
        self.carrierLabel.setText(_translate("Form", "<html><head/><body><p><img src=\":/translation_images/hieroglyphics.jpg\"/></p></body></html>"))

