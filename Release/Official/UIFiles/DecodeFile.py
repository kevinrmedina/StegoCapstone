

class DecodeFile(QtWidgets.QWidget):
    def __init__(self, imageData, config, CarrierDir):
        super (DecodeFile, self).__init__()
        uic.loadUi('DecodeFile.ui', self)
        