import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QPixmap
from fileservice import FileService
from UIFiles.HomePage import HomePage
from UIFiles.BrowsePage import BrowsePage
from UIFiles.EncodeDecodePage import EncodeDecodePage
from UIFiles.ChooseCarrierType import ChooseCarrierTypePage
from UIFiles.Translation import TanslationPage
#from UIFiles.EncryptionPage import EncryptionPage
from UIFiles.TextPayloadPage import TextPayloadPage

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
ImageFileName = ""  # used to store image file path and display image in UI


class MainWindow(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(object)  # signal used by controller to switch windows

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Main Window')

        layout = QtWidgets.QVBoxLayout()

        imageLabel = QtWidgets.QLabel(self)
        pixmap = QPixmap("web.png")
        imageLabel.setPixmap(pixmap)
        imageLabel.resize(pixmap.width(), pixmap.height())
        imageLabel.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        layout.addWidget(imageLabel)

        # self.line_edit = QtWidgets.QLineEdit()
        # layout.addWidget(self.line_edit)

        self.button = QtWidgets.QPushButton('Browse')
        self.button.setMaximumWidth(500 / 3)
        self.button.setContentsMargins(0, 0, 0, 10)

        self.button.clicked.connect(self.openFileBrowser)
        layout.addWidget(self.button, alignment=QtCore.Qt.AlignCenter)

        self.switchbutton = QtWidgets.QPushButton('Next')
        self.switchbutton.setMaximumWidth(500 / 3)
        self.switchbutton.setContentsMargins(0, 0, 0, 10)
        self.switchbutton.clicked.connect(self.switch)
        layout.addWidget(self.switchbutton, alignment=QtCore.Qt.AlignCenter)

        # TODO look for current position and pass as x and y values to keep window position
        self.resize(WINDOWWIDTH, WINDOWHEIGHT)
        self.center()
        self.setLayout(layout)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def switch(self):
        # self.switch_window.emit(self.line_edit.text())
        self.switch_window.emit(self.ImageData)

    def openFileBrowser(self):
        ImageFileName = FileService.openFileNameDialog(self, self)
        if (ImageFileName != None or ImageFileName != ""):
            file = FileService.openFileContent(self, ImageFileName)
        self.ImageData = file.read()


class WindowTwo(QtWidgets.QWidget):

    def __init__(self, imageData):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window Two')

        layout = QtWidgets.QGridLayout()

        radiobuttons = QtWidgets.QVBoxLayout()
        nextprevButtons = QtWidgets.QHBoxLayout()
        
        prevButton = QtWidgets.QPushButton("Prev")
        nextButton = QtWidgets.QPushButton("Next")
        
        nextButton.clicked.connect(self.NextButtonClicked)
        prevButton.clicked.connect(self.PrevButtonClicked)

        nextprevButtons.addWidget(prevButton)
        nextprevButtons.addWidget(nextButton)
        
        layout.addLayout(nextprevButtons, 1, 1)
        # self.label = QtWidgets.QLabel(text)
        # layout.addWidget(self.label)
        imageLabel = QtWidgets.QLabel(self)
        pixmap = QPixmap()
        pixmap.loadFromData(imageData)
        imageLabel.setPixmap(pixmap)
        imageLabel.resize(pixmap.width(), pixmap.height())
        imageLabel.setAlignment(QtCore.Qt.AlignCenter)  # center image label
        imageLabel.setStyleSheet("border-style: solid; border-width: 2px; border-color: black;")
        layout.addWidget(imageLabel, 0, 1)

        ##Encode/Decode radio buttons
        radiobutton = QtWidgets.QRadioButton("Encode")
        radiobutton.setChecked(True)
        radiobutton.toggled.connect(self.onClicked)
        radiobuttons.addWidget(radiobutton)

        radiobutton = QtWidgets.QRadioButton("Decode")
        radiobutton.toggled.connect(self.onClicked)
        radiobuttons.addWidget(radiobutton)
        radiobuttons.setContentsMargins(20, 0, 0, 0)
        layout.addLayout(radiobuttons, 0, 0)

        # TODO look for current position and pass as x and y values to keep window position
        self.resize(WINDOWWIDTH, WINDOWHEIGHT)
        self.center()
        self.setLayout(layout)

        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)

    def onClicked(self):
        radioButton = self.sender()
        # if radioButton.isChecked():
        #     print("Country is %s" % (radioButton.value))

    def NextButtonClicked(self):
        print("")

    def PrevButtonClicked(self):
        print("")

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class Login(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Login')

        layout = QtWidgets.QGridLayout()

        self.button = QtWidgets.QPushButton('Login')
        self.button.clicked.connect(self.login)

        layout.addWidget(self.button)
        # TODO look for current position and pass as x and y values to keep window position
        self.resize(500, 500)
        self.center()
        self.setLayout(layout)

    def login(self):
        self.switch_window.emit()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class Controller:
    
    def __init__(self):
        pass

    def show_login(self):
        self.login = Login()
        self.login.switch_window.connect(self.show_main)
        self.home.close()
        self.login.show()

    def show_home(self):
        self.home = HomePage()
        self.home.switch_window.connect(self.showBrowsePage)
        self.home.show()

    def showBrowsePage(self):
        self.browsepage = BrowsePage()
        self.browsepage.switch_window.connect(self.ShowDecodeEncodePage)
        self.home.close()
        self.browsepage.show()
    
    def ShowDecodeEncodePage(self, imageData, ImageDir):
        self.deencodepage = EncodeDecodePage(imageData, ImageDir)
        self.deencodepage.switch_window.connect(self.ShowChoosePayloadTypePage)
        self.browsepage.close()
        self.deencodepage.show()

    def ShowChoosePayloadTypePage(self, imageData, config, ImageDir):
        self.choosecarrier = ChooseCarrierTypePage(imageData, config, ImageDir)
        self.choosecarrier.switch_window.connect(self.ShowTextPayloadPage)
        self.deencodepage.close()
        self.choosecarrier.show()
    
    def ChoosePayloadTypeNextButton(self, imageData, config, CarrierDir):
        self.encryption = EncryptionPage(imageData, config, CarrierDir)
        self.encryption.switch_window.connect(self.ShowTextPayloadPage)
        self.choosecarrier.close()
        self.encryption.show()


    def ShowTextPayloadPage(self, imageData, config, CarrierDir):
        self.textpayload = TextPayloadPage(imageData, config, CarrierDir)
        self.textpayload.show()
        #self.encryption.close()
        self.choosecarrier.close()

    def show_main(self):
        self.window = MainWindow()
        self.window.switch_window.connect(self.show_window_two)
        self.login.close()
        self.window.show()

    def show_window_two(self, imageData):
        self.window_two = WindowTwo(imageData)
        self.window.close()
        self.window_two.show()

    def OpenTranslationPane():
        self.translation = TranslationPage()
        self.translation.show()





def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    # Add Main Window for 
    # extractAction = QtWidgets.QAction("Open Translation Pane", self)
    #     extractAction.setShortcut("Ctrl+Q")
    #     extractAction.setStatusTip('Leave The App')
    #     #extractAction.triggered.connect(controller.OpenTranslationPane)
        
    #     mainMenu = self.menuBar()
    #     fileMenu = mainMenu.addMenu('&File')
    #     fileMenu.addAction(extractAction)
    #     self.show()
    # self.setCentralWidget(self.Form)
    controller.show_home()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
