#!/usr/bin/env python

import sys
import UIFiles.morseDecipher
from PyQt5 import QtWidgets, uic, QtGui

class TanslationPane(QtWidgets.QDialog):
    def __init__(self):
        super (TanslationPane, self).__init__()
        uic.loadUi('./UIFiles/Translation.ui', self)

        # Defining object pointers and connecting to their Methods
        #
        ##language Key pointers and methods
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
