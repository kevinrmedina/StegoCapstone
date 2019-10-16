# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIFiles/ChooseCarrierType.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
from fileservice import FileService 
from PyQt5 import QtCore, QtGui, QtWidgets
from UIFiles import DesManager
import re

class ChoosePayloadTypePage(QtCore.QObject):

    show_encode_file = QtCore.pyqtSignal(object, object, object, object)  # Add switch_window signal for controller to use to switch layouts
    switch_previous = QtCore.pyqtSignal(object, object)  # Add switch_window signal for controller to use to switch layouts
    show_encode_text = QtCore.pyqtSignal(object, object, object)
    show_decode_text = QtCore.pyqtSignal(object, object, object)
    show_decode_file = QtCore.pyqtSignal(object, object, object)
    def __init__(self, imageData, config, CarrierDir):
        QtCore.QObject.__init__(self) # call init from parent class
        self.Form = QtWidgets.QWidget() # initialize widget (this is what Qt shows)
        self.imagedata = imageData
        self.carrierDir = CarrierDir
        self.Config = config
        self.setupUi(self.Form) # sets up ui in Form widget

    def show(self): # implement show method for controller to use 
        self.Form.show()

    def EmitSwitchNext(self): # implement event that will emit the switch window signal 
        if (self.Config == "Encode"):
            if (self.fileRadioButton.isChecked()):
                #Show Browser to select payload and pass it to next page (pass payload directory)
                payloadDir = FileService.openAnyFileNameDialog(self.Form, self.Form)
                if (payloadDir != ''):
                    #### Adding cryptographic components
                    if(self.cryptographyCheckBox.isChecked()):
                        if(self.algorithmComboBox.currentIndex() == 0): #AES
                            print('AES')
                        elif(self.algorithmComboBox.currentIndex() == 1): #DES
                            payloadDirCrypt = re.sub('\.', 'Crypted.', payloadDir)
                            password = self.encryptionKeyTextEdit.toPlainText()
                            DesManager.write_encrypted_text(password.encode('ascii'), payloadDirCrypt, payloadDir) 
                            self.show_encode_file.emit(self.imagedata, self.Config, self.carrierDir, payloadDirCrypt)
                            
                        elif(self.algorithmComboBox.currentIndex() == 2): #RSA
                            print('RSA')


                    self.show_encode_file.emit(self.imagedata, self.Config, self.carrierDir, payloadDir)
            else:
                self.show_encode_text.emit(self.imagedata, self.Config, self.carrierDir)
        else:
            if (self.fileRadioButton.isChecked()):
                self.show_decode_file.emit(self.imagedata, self.Config, self.carrierDir)
            else:
                self.show_decode_text.emit(self.imagedata, self.Config, self.carrierDir)
    
    def EmitSwitchPrevious(self): # implement event that will emit the switch window signal 
        self.switch_previous.emit(self.imagedata, self.carrierDir)
    
    def close(self): # implement close method used by controller
        self.Form.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(639, 550)
        Form.setFixedSize(750, 550)
       # self.verticalLayoutWidget = QtWidgets.QWidget(Form)
       # self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 100, 201, 272))
       # self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
       # self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
       # self.verticalLayout.setContentsMargins(10, 10, 10, 10)
       # self.verticalLayout.setObjectName("verticalLayout")
       # self.verticalLayout_2 = QtWidgets.QVBoxLayout()
       # self.verticalLayout_2.setObjectName("verticalLayout_2")
       # self.textRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
       # self.textRadioButton.setObjectName("textRadioButton")
       # self.verticalLayout_2.addWidget(self.textRadioButton)
       # self.textRadioButton.setChecked(True)
       # self.verticalLayout.addLayout(self.verticalLayout_2)
       # self.verticalLayout_3 = QtWidgets.QVBoxLayout()
       # self.verticalLayout_3.setObjectName("verticalLayout_3")
       # self.fileRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
       # self.fileRadioButton.setObjectName("fileRadioButton")
       # self.verticalLayout_3.addWidget(self.fileRadioButton)
       # self.verticalLayout.addLayout(self.verticalLayout_3)
       # self.verticalLayout_4 = QtWidgets.QVBoxLayout()
       # self.verticalLayout_4.setObjectName("verticalLayout_4")
       # self.cryptographyCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
       # self.cryptographyCheckBox.setObjectName("cryptographyCheckBox")
       # self.verticalLayout_4.addWidget(self.cryptographyCheckBox)
       # self.cryptographyCheckBox.clicked.connect(self.cryptographyCheckBoxClicked)
       # self.algorithmComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
       # self.algorithmComboBox.setObjectName("algorithmComboBox")
       # self.verticalLayout_4.addWidget(self.algorithmComboBox)
       # self.algorithmComboBox.setEnabled(False)
       # self.verticalLayout.addLayout(self.verticalLayout_4)
       # self.encryptionKeyTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
       # self.encryptionKeyTextEdit.setMaximumSize(QtCore.QSize(16777215, 45))
       # self.encryptionKeyTextEdit.setObjectName("encryptionKeyTextEdit")
       # self.verticalLayout.addWidget(self.encryptionKeyTextEdit)
       # self.encryptionKeyTextEdit.setEnabled(False)
       # self.label = QtWidgets.QLabel(Form)
       # self.label.setGeometry(QtCore.QRect(388, 80, 221, 271))
       # # self.label.setText("")
       # pixmap = QtGui.QPixmap()
       # pixmap.loadFromData(self.imagedata)
       # self.label.setPixmap(pixmap)
       # # self.label.resize(pixmap.width(), pixmap.height())
       # self.label.setAlignment(QtCore.Qt.AlignCenter)  # center image label
       # self.label.setStyleSheet("border-style: solid; border-width: 2px; border-color: black;")
       # self.label.setObjectName("label")
       # self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
       # self.horizontalLayoutWidget.setGeometry(QtCore.QRect(390, 370, 221, 80))
       # self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
       # self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
       # self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
       # self.horizontalLayout.setObjectName("horizontalLayout")
       # self.previousButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
       # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
       # sizePolicy.setHorizontalStretch(0)
       # sizePolicy.setVerticalStretch(0)
       # sizePolicy.setHeightForWidth(self.previousButton.sizePolicy().hasHeightForWidth())
       # self.previousButton.setSizePolicy(sizePolicy)
       # self.previousButton.setMinimumSize(QtCore.QSize(0, 50))
       # self.previousButton.setObjectName("previousButton")
       # self.horizontalLayout.addWidget(self.previousButton)
       # self.nextButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
       # self.previousButton.clicked.connect(self.EmitSwitchPrevious)
       # self.nextButton.setMinimumSize(QtCore.QSize(0, 50))
       # self.nextButton.setObjectName("nextButton")
       # self.horizontalLayout.addWidget(self.nextButton)
       # self.nextButton.clicked.connect(self.EmitSwitchNext)
       # self.ActionLabel = QtWidgets.QLabel(Form)
       # self.ActionLabel.setGeometry(QtCore.QRect(20, 20, 611, 20))
       # self.ActionLabel.setAlignment(QtCore.Qt.AlignCenter)
       # self.ActionLabel.setObjectName("ActionLabel")
       # self.retranslateUi(Form)
       # QtCore.QMetaObject.connectSlotsByName(Form)

        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 130, 201, 272))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.textRadioButton.setObjectName("textRadioButton")
        self.textRadioButton.setChecked(True)
        self.verticalLayout_2.addWidget(self.textRadioButton)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fileRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.fileRadioButton.setObjectName("fileRadioButton")
        self.verticalLayout_3.addWidget(self.fileRadioButton)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cryptographyCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.cryptographyCheckBox.setObjectName("cryptographyCheckBox")
        self.verticalLayout_4.addWidget(self.cryptographyCheckBox)
        self.algorithmComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.algorithmComboBox.setObjectName("algorithmComboBox")
        self.algorithmComboBox.setEnabled(False)
        self.algorithmComboBox.addItems(['AES', 'DES', 'RSA'])
        self.cryptographyCheckBox.clicked.connect(self.cryptographyCheckBoxClicked)
        self.verticalLayout_4.addWidget(self.algorithmComboBox)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.encryptionKeyTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.encryptionKeyTextEdit.setMaximumSize(QtCore.QSize(16777215, 45))
        self.encryptionKeyTextEdit.setObjectName("encryptionKeyTextEdit")
        self.encryptionKeyTextEdit.setEnabled(False)
        self.verticalLayout.addWidget(self.encryptionKeyTextEdit)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(490, 450, 221, 80))
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
        self.previousButton.clicked.connect(self.EmitSwitchPrevious)
        self.horizontalLayout.addWidget(self.previousButton)
        self.nextButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.nextButton.setMinimumSize(QtCore.QSize(0, 50))
        self.nextButton.setObjectName("nextButton")
        self.nextButton.clicked.connect(self.EmitSwitchNext)
        self.horizontalLayout.addWidget(self.nextButton)
        self.ActionLabel = QtWidgets.QLabel(Form)
        self.ActionLabel.setGeometry(QtCore.QRect(67, 20, 611, 20))
        self.ActionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ActionLabel.setObjectName("ActionLabel")
        self.carrierScrollArea = QtWidgets.QScrollArea(Form)
        self.carrierScrollArea.setGeometry(QtCore.QRect(370, 70, 362, 361))
        self.carrierScrollArea.setWidgetResizable(True)
        self.carrierScrollArea.setObjectName("carrierScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 360, 359))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.carrierLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.carrierLabel.setObjectName("carrierLabel")
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(self.imagedata)
        self.carrierLabel.setPixmap(pixmap)
        self.gridLayout_3.addWidget(self.carrierLabel, 0, 0, 1, 1)
        self.carrierScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textRadioButton.setText(_translate("Form", "Text"))
        self.fileRadioButton.setText(_translate("Form", "File"))
        self.cryptographyCheckBox.setText(_translate("Form", "Cryptography"))
        self.encryptionKeyTextEdit.setPlainText(_translate("Form", "Encryption Key\n"
""))
        self.previousButton.setText(_translate("Form", "Prev"))
        self.nextButton.setText(_translate("Form", "Next"))
        self.ActionLabel.setText(_translate("Form", self.Config))

    def cryptographyCheckBoxClicked(self):
        if (self.cryptographyCheckBox.isChecked()):
            self.algorithmComboBox.setEnabled(True)
            self.encryptionKeyTextEdit.setEnabled(True)
        else:
            self.algorithmComboBox.setEnabled(False)
            self.encryptionKeyTextEdit.setEnabled(False)
