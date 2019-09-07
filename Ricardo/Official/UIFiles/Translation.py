# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIFiles/Translation.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class TanslationPage(QtCore.QObject):
    switch_window = QtCore.pyqtSignal()  # Add switch_window signal for controller to use to switch layouts
    def __init__(self):
        QtCore.QObject.__init__(self) # call init from parent class
        self.Form = QtWidgets.QWidget() # initialize widget (this is what Qt shows)
        
        self.setupUi(self.Form) # sets up ui in Form widget

    def show(self): # implement show method for controller to use 
        self.Form.show()

    def EmitSwitch(self): # implement event that will emit the switch window signal
        self.switch_window.emit(self.imagedata, config)
    
    def close(self): # implement close method used by controller
        self.Form.close()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(762, 567)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.languageKeyComboBox = QtWidgets.QComboBox(Dialog)
        self.languageKeyComboBox.setObjectName("languageKeyComboBox")
        self.languageKeyComboBox.addItem("")
        self.languageKeyComboBox.addItem("")
        self.languageKeyComboBox.addItem("")
        self.languageKeyComboBox.addItem("")
        self.languageKeyComboBox.addItem("")
        self.gridLayout.addWidget(self.languageKeyComboBox, 1, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 3, 1)
        self.keyScrollArea = QtWidgets.QScrollArea(Dialog)
        self.keyScrollArea.setWidgetResizable(True)
        self.keyScrollArea.setObjectName("keyScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 624, 800))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.languageKeyLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.languageKeyLabel.setObjectName("languageKeyLabel")
        self.gridLayout_3.addWidget(self.languageKeyLabel, 0, 0, 1, 1)
        self.keyScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.keyScrollArea, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectedImageScrollArea = QtWidgets.QScrollArea(Dialog)
        self.selectedImageScrollArea.setWidgetResizable(True)
        self.selectedImageScrollArea.setObjectName("selectedImageScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 358, 230))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.selectedImageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.selectedImageLabel.setObjectName("selectedImageLabel")
        self.gridLayout_2.addWidget(self.selectedImageLabel, 0, 0, 1, 1)
        self.selectedImageScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.selectedImageScrollArea)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.selectImageButton = QtWidgets.QPushButton(Dialog)
        self.selectImageButton.setObjectName("selectImageButton")
        self.gridLayout.addWidget(self.selectImageButton, 3, 1, 1, 1)
        self.translateMorseCodeButton = QtWidgets.QPushButton(Dialog)
        self.translateMorseCodeButton.setObjectName("translateMorseCodeButton")
        self.gridLayout.addWidget(self.translateMorseCodeButton, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.languageKeyComboBox = self.findChild(QtWidgets.QComboBox, 'languageKeyComboBox')
        self.languageKeyComboBox.activated[str].connect(self.keyChange)
        self.languageKeyLabel.setPixmap(QtGui.QPixmap("hieroglyphics.jpg"))
        self.languageKeyLabel = self.findChild(QtWidgets.QLabel, 'languageKeyLabel')
        
        ##User selected image pointers and methods
        self.selectedImageLabel = self.findChild(QtWidgets.QLabel, 'selectedImageLabel')
        self.selectImageButton = self.findChild(QtWidgets.QPushButton, 'selectImageButton')
        ##Morse Code Translation pointers and methods
        self.translateMorseCodeButton = self.findChild(QtWidgets.QPushButton, 'translateMorseCodeButton')
        self.translateMorseCodeButton.clicked.connect(self.morseCodeFunction)
        self.show()
    
        self.textEdit = self.findChild(QtWidgets.QTextEdit, 'textEdit')
    ##Function that changed the language key according to the selected option on the comboBox 
    def keyChange(self, text):
        if self.languageKeyComboBox.currentText() == 'Hieroglyphics':
            self.languageKeyLabel.setPixmap(QtGui.QPixmap("hieroglyphics.jpg"))
        elif self.languageKeyComboBox.currentText() == 'Unknown Pokemon':
            self.languageKeyLabel.setPixmap(QtGui.QPixmap("unknown.jpeg"))
        elif self.languageKeyComboBox.currentText() == 'Morse Code':
            self.languageKeyLabel.setPixmap(QtGui.QPixmap("morseCode.jpeg"))
        elif self.languageKeyComboBox.currentText() == 'Wingdings':
            self.languageKeyLabel.setPixmap(QtGui.QPixmap("wingdings.gif"))
        elif self.languageKeyComboBox.currentText() == 'PigPen':
            self.languageKeyLabel.setPixmap(QtGui.QPixmap("pigpen.gif"))
    
    def morseCodeFunction(self):
        count = 0
        text = self.textEdit.toPlainText() 
        text = text.encode('ascii', 'ignore')
        for character in text: 
            if character != '.' and character != '-' and character != '/' and character != ' ':
                count += 1
        if count >= 1:
            self.textEdit.clear()
            inputText = str.upper(str(text))
            self.textEdit.append(morseDecipher.encrypt(inputText.replace('\n', '')))
        else:
            self.textEdit.clear()
            self.textEdit.append(morseDecipher.decrypt(str(text) + ' '))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Translation"))
        self.languageKeyComboBox.setItemText(0, _translate("Dialog", "Hieroglyphics"))
        self.languageKeyComboBox.setItemText(1, _translate("Dialog", "Unknown Pokemon"))
        self.languageKeyComboBox.setItemText(2, _translate("Dialog", "Morse Code"))
        self.languageKeyComboBox.setItemText(3, _translate("Dialog", "Wingdings"))
        self.languageKeyComboBox.setItemText(4, _translate("Dialog", "PigPen"))
        #self.languageKeyLabel.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/translation_images/hieroglyphics.jpg\"/></p></body></html>"))
        #self.selectedImageLabel.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/Resource/puppy.png\"/></p></body></html>"))
        self.selectImageButton.setText(_translate("Dialog", "Select Image"))
        self.translateMorseCodeButton.setText(_translate("Dialog", "Translate Morse Code"))

