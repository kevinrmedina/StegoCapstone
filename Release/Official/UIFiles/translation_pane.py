#!/usr/bin/env python

import sys
import os
import time
import subprocess
from fileservice import FileService
#from UIFiles import morseDecipher
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QFileDialog

class TranslationPane(QtWidgets.QDialog):
    def __init__(self):
        super (TranslationPane, self).__init__()
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
        selectedImage = FileService.openFileNameDialog(self, self) 
        print(selectedImage)
        selectedImage = str(selectedImage)
        print(selectedImage)
        if (selectedImage != None or selectedImage != ""):
            self.selectedImageLabel.setPixmap(QtGui.QPixmap(selectedImage))

    def morseCodeFunction(self):
        count = 0
        text = self.textEdit.toPlainText() 
        #text = text.encode('ascii', 'ignore')
        for character in text: 
            if character != '.' and character != '-' and character != '/' and character != ' ':
                count += 1
        if count >= 1:
            self.textEdit.clear()
            inputText1 = str.upper(str(text))
            inputText = inputText1.replace("\n", " ")
            command = 'python UIFiles/morseDecipher.py 1 '
            command = command.split() + [str(inputText)]
            process = subprocess.Popen(command)
            process.wait()
            if os.path.exists('/tmp/morseCodeTemp'):
                time.sleep(5)
            tempFile = open('/tmp/morseCodeTemp', 'r')
            morseCode = tempFile.read()
            tempFile.close()
            self.textEdit.append(morseCode)
            os.remove('/tmp/morseCodeTemp')

        else:
            self.textEdit.clear()
            inputText1 = str.upper(str(text))
            inputText = inputText1.replace("\n", " ") 
            command = 'python UIFiles/morseDecipher.py 2 '
            command = command.split() + [inputText]
            process = subprocess.Popen(command)
            process.wait()
            if os.path.exists('/tmp/morseCodeTemp'):
                time.sleep(5)
            tempFile = open('/tmp/morseCodeTemp', 'r')
            asciiText = tempFile.read()
            tempFile.close()
            self.textEdit.append(asciiText)
            os.remove('/tmp/morseCodeTemp')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    translation = TranslationPane()
    translation.show()
    sys.exit(app.exec_())
