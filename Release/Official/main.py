import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QPixmap
from fileservice import FileService
from UIFiles.HomePage import HomePage
from UIFiles.BrowsePage import BrowsePage
from UIFiles.EncodeDecodePage import EncodeDecodePage
from UIFiles.ChoosePayloadType import ChoosePayloadTypePage
from UIFiles.Translation import TanslationPage
#from UIFiles.EncryptionPage import EncryptionPage
from UIFiles.TextPayloadPage import TextPayloadPage
from UIFiles.EncodeFile import EncodeFile
from UIFiles.DecodeFile import DecodeFile
from UIFiles.DecodeText import DecodeText
from UIFiles.EncodeText import EncodeText
from UIFiles.ResultScreen import ResultScreen


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
    
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        pass

    def show_login(self):
        self.login = Login()
        self.login.switch_window.connect(self.show_main)
        self.home.close()
        self.login.show()

    def show_home(self):
        self.home = HomePage()
        self.MainWindow.setCentralWidget(self.home.Form)
        self.home.switch_window.connect(self.showBrowsePage)
        self.home.show()

    def showBrowsePage(self):
        self.browsepage = BrowsePage()
        self.MainWindow.setCentralWidget(self.browsepage.Form)
        self.browsepage.switch_window.connect(self.ShowDecodeEncodePage)
        self.home.close()
        self.browsepage.show()
    
    def ShowDecodeEncodePage(self, imageData, ImageDir):
        self.deencodepage = EncodeDecodePage(imageData, ImageDir)
        self.MainWindow.setCentralWidget(self.deencodepage.Form)
        self.deencodepage.switch_window.connect(self.ShowChoosePayloadTypePage)
        self.deencodepage.previous_clicked.connect(self.showBrowsePage)
        self.browsepage.close()
        self.deencodepage.show()

    def ShowChoosePayloadTypePage(self, imageData, config, ImageDir):
        self.choosepayload = ChoosePayloadTypePage(imageData, config, ImageDir)
        self.choosepayload.show_encode_file.connect(self.ShowEncodeFile)
        self.choosepayload.show_decode_file.connect(self.ShowDecodeFile)
        self.choosepayload.show_decode_text.connect(self.ShowDecodeText)
        self.choosepayload.show_encode_text.connect(self.ShowEncodeText)
        self.choosepayload.switch_previous.connect(self.ShowDecodeEncodePage)
        self.MainWindow.setCentralWidget(self.choosepayload.Form)
        self.deencodepage.close()
        self.choosepayload.show()
    
    def ShowTextPayloadPage(self, imageData, config, CarrierDir):
        self.textpayload = TextPayloadPage(imageData, config, CarrierDir)
        self.MainWindow.setCentralWidget(self.textpayload.Form)
        self.textpayload.show()
        #self.encryption.close()
        self.choosepayload.close()
    
    def ShowEncodeFile(self, imageData, config, CarrierDir, payloadDir):      
        self.encodefile = EncodeFile(imageData, config, CarrierDir, payloadDir)
        self.MainWindow.setCentralWidget(self.encodefile)
        self.encodefile.show()
        self.choosepayload.close()
     
    def ShowDecodeFile(self, imageData, config, CarrierDir):
        self.decodefile = DecodeFile(imageData, config, CarrierDir)
        self.MainWindow.setCentralWidget(self.decodefile)
        self.decodefile.show()
        self.choosepayload.close()
    
    def ShowEncodeText(self, imageData, config, CarrierDir):
        self.encodetext = EncodeText(imageData, config, CarrierDir)
        self.encodetext.show_Result.connect(self.ShowResult)
        self.MainWindow.setCentralWidget(self.encodetext)
        self.encodetext.show()
        self.choosepayload.close()
    
    def ShowResult(self, EncodedImageResultDir, imageData, CarrierDir, config, lastPage, payloadDir=None):
        self.resultscreen = ResultScreen(EncodedImageResultDir, imageData, CarrierDir, config, lastPage, payloadDir)
        self.resultscreen.switch_mainmenu.connect(self.show_home)
        self.resultscreen.switch_previous.connect(self.ResultGoBack)
        self.MainWindow.setCentralWidget(self.resultscreen)
        self.resultscreen.show()

    def ResultGoBack(self, imageData, config, CarrierDir, lastPage, payloadDir):
        if (lastPage == 1):
            ShowEncodeFile(imageData, config, CarrierDir, payloadDir)
        elif (lastPage == 2):
            ShowDecodeFile(imageData, config, CarrierDir)
        elif (lastPage == 3):
            ShowEncodeText(imageData, config, CarrierDir)
        elif (lastPage == 4):
            ShowDecodeText(imageData, config, CarrierDir)

    def ShowDecodeText(self, imageData, config, CarrierDir):
        self.decodetext = DecodeText(imageData, config, CarrierDir)
        self.MainWindow.setCentralWidget(self.decodetext)
        self.decodetext.show()
        self.choosepayload.close()


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
    
    MainWindow = QtWidgets.QMainWindow()
    controller = Controller(MainWindow)
    #Menu option called Open Translation Pane to 'File' menu
    extractAction = QtWidgets.QAction("Open Translation Pane", MainWindow)
    extractAction.setShortcut("Ctrl+Q")
    extractAction.setStatusTip('Leave The App')
    extractAction.triggered.connect(controller.OpenTranslationPane)
    mainMenu = MainWindow.menuBar()
    fileMenu = mainMenu.addMenu('&File')
    fileMenu.addAction(extractAction)
    MainWindow.show()
    MainWindow.resize(640, 500)
    #MainWindow.setCentralWidget(self.Form)
    controller.show_home()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
