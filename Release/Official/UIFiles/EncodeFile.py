import sys
import morseDecipher
from PyQt5 import QtWidgets, uic, QtGui

class EncodeFile(QtWidgets.QWidget):
    def __init__(self, imageData, config, CarrierDir):
        super (EncodeImage, self).__init__()
        uic.loadUi('EncodeImage.ui', self)