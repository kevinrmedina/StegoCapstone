#!/usr/bin/env python

import sys
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QFileDialog

class TanslationPane(QtWidgets.QDialog):
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
            self.textEdit.append(encrypt(inputText.replace('\n', '')))
        else:
            self.textEdit.clear()
            self.textEdit.append(decrypt(str(text) + ' '))


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..',
                    'E':'.', 'F':'..-.',
                    'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---',
                    'K':'-.-', 'L':'.-..',
                    'M':'--', 'N':'-.', 'O':'---',
                    'P':'.--.', 'Q':'--.-', 'R':'.-.',
                    'S':'...', 'T':'-', 'U':'..-', 'V':'...-',
                    'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----',
                    '2':'..---', '3':'...--', '4':'....-', '5':'.....',
                    '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ':'/', '':''}

def encrypt(message):
    #message = 'SOS'
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += '/'
    return cipher

def decrypt(message):
    #message = '...'
    decipher = ''
    citext = ''

    for letter in message:
        if (letter != ' '):
            citext += letter

        else:
            decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
            citext = ''
    return decipher
    #print decipher


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    translation = TanslationPane()
    translation.show()
    sys.exit(app.exec_())