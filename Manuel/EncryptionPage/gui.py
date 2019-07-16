from PyQt5.QtWidgets import *
import encryption


class Gui:

    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.window.resize(480, 360)
        self.window.setWindowTitle('Encrypt/Decrypt')
        self.layout = QGridLayout()
        self.encryptButton = QRadioButton("Encrypt")
        self.encryptButton.setChecked(True)
        self.decryptButton = QRadioButton("Decrypt")
        self.algoCB = QComboBox()
        self.algoCB.addItems(["RSA", "AES", "DES"])
        self.label = QLabel("Key:")
        self.keyBox = QTextEdit()
        self.prevButton = QPushButton("Previous")
        self.nextButton = QPushButton("Next")
        # Place elements in layout
        self.layout.addWidget(self.encryptButton, 1, 0)
        self.layout.addWidget(self.decryptButton, 1, 1)
        self.layout.addWidget(self.algoCB, 2, 0, 1, 0)
        self.layout.addWidget(self.label, 3, 0)
        self.layout.addWidget(self.keyBox, 4, 0, 1, 0)
        self.layout.addWidget(self.prevButton, 5, 0)
        self.layout.addWidget(self.nextButton, 5, 1)
        # Listeners
        self.nextButton.clicked.connect(lambda: self.next_button_listener())
        self.prevButton.clicked.connect(lambda: prev_button_listener())

    def private_execute(self):
        self.window.setLayout(self.layout)
        self.window.show()
        self.app.exec_()

    def next_button_listener(self):
        plaintext = "Python rocks!"
        cypher_text = b'>\xfc\x1f\x16x\x87\xb2\x93\x0e\xfcH\x02\xd59VQ'

        encrypt = encryption.Encryption(self.keyBox.toPlainText())

        if self.encryptButton.isChecked():
            if self.algoCB.itemText(self.algoCB.currentIndex()) == "DES":
                print('Encrypted text is: ', end='')
                print(encrypt.encrypt(plaintext))
            else:
                print("Not yet implemented")
        elif self.decryptButton.isChecked():
            if self.algoCB.itemText(self.algoCB.currentIndex()) == "DES":
                print('Decrypted text is: ', end='')
                print(encrypt.decrypt(cypher_text))
            else:
                print("Not yet implemented")
        else:
            print("Error!")
        print("Current combo box selection is: " + self.algoCB.itemText(self.algoCB.currentIndex()))
        print("Key contains: " + self.keyBox.toPlainText())
        print("")


def prev_button_listener():
    print("Previous button clicked!")
