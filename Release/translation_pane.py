#!/usr/bin/env python

import sys
import morseDecipher
from PyQt5 import QtWidgets, uic, QtGui

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super (Ui, self).__init__()
        uic.loadUi('Translation.ui', self)

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
        ##Morse Code Translation pointers and methods
        self.translateMorseCodeButton = self.findChild(QtWidgets.QPushButton, 'translateMorseCodeButton')
        self.translateMorseCodeButton.clicked.connect(self.morseCodeFunction)
        self.show()
    
        self.textEdit = self.findChild(QtWidgets.QTextEdit, 'textEdit')
    ##Function that changed the language key according to the selected option on the comboBox 
        self.selectImageButton = self.findChild(QtWidgets.QPushButton,
                "selectImageButton")
        self.selectImageButton.clicked.connect(self.selectImage)

        self.selectedImageLabel = self.findChild(QtWidgets.QLabel,
                "selectedImageLabel")
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
    
    def selectImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,
                "QFileDialog.getOpenFileName()", "", "*.png *.jpg *.jpeg *.gif *.bmp", options = options)
        print(fileName)
        self.selectedImageLabel.setPixmap(QtGui.QPixmap(fileName))
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
