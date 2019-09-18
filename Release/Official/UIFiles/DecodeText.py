import sys
import morseDecipher
from PyQt5 import QtWidgets, uic, QtGui

class DecodeText(QtWidgets.QWidget):
    def __init__(self, imageData, config, CarrierDir):
        super (DecodeText, self).__init__()
        uic.loadUi('DecodeText.ui', self)