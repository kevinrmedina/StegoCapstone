#!/usr/bin/env python

import sys
#import UIFiles.morseDecipher
from UIFiles import morseDecipher
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QFileDialog

class TranslationPane(QtWidgets.QDialog):
    def __init__(self):
        super (TanslationPane, self).__init__()
        uic.loadUi('./UIFiles/Translation.ui', self)

        # Defining object pointers and connecting to their Methods
        #
        ##language Key pointers and methods
        self.languageKeyComboBox = self.findChild(QtWidgets.QComboBox, 'languageKeyComboBox')
        self.languageKeyComboBox.activated[str].connect(self.keyChange)
        self.languageKeyLabel.setPixmap(QtGui.QPixmap("./languageKeys/hieroglyphics.jpg"))
        self.languageKeyLabel = self.findChild(QtWidgets.QLabel, 'languageKeyLabel')
        
        ##User selected image pointers and methods
        self.selectedImageLabel = self.findChild(QtWidgets.QLabel, 'selectedImageLabel')
        self.selectImageButton = self.findChild(QtWidgets.QPushButton, 'selectImageButton')
        self.selectImageButton.clicked.connect(self.selectImage)
        ##Morse Code Translation pointers and methods
        self.translateMorseCodeButton = self.findChild(QtWidgets.QPushButton, 'translateMorseCodeButton')
        self.translateMorseCodeButton.clicked.connect(self.morseCodeFunction)
        self.show()
    
        self.textEdit = self.findChild(QtWidgets.QTextEdit, 'textEdit')
    ##Function that changed the language key according to the selected option on the comboBox 
    def keyChange(self, text):
        if self.languageKeyComboBox.currentText() == 'Hieroglyphics':
            self.languageKeyLabel.setPixmap(QtGui.QPixmap("./languageKeys/hieroglyphics.jpg"))
        elif self.languageKeyComboBox.currentText() == 'Unknown Pokemon':
            self.languageKeyLabel.setPixmap(QtGui.QPixmap("./languageKeys/unknown.jpeg"))
        elif self.languageKeyComboBox.currentText() == 'Morse Code':
            self.languageKeyLabel.setPixmap(QtGui.QPixmap("./languageKeys/morseCode.jpeg"))
        elif self.languageKeyComboBox.currentText() == 'Wingdings':
            self.languageKeyLabel.setPixmap(QtGui.QPixmap("./languageKeys/wingdings.gif"))
        elif self.languageKeyComboBox.currentText() == 'PigPen':
            self.languageKeyLabel.setPixmap(QtGui.QPixmap("./languageKeys/pigpen.gif"))
    
    def selectImage(self):
        selectedImage = QFileDialog.getOpenFileName(self, "Open File", " ", "*.png *.jpg *.jpeg *.bmp *.gif *.tif *.dib *.jpe *.jfif *.tiff")
        selectedImage = str(selectedImage)
        if (selectedImage != None and selectedImage != ""):
            self.selectedImageLabel.setPixmap(QtGui.QPixmap(selectedImage))

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
