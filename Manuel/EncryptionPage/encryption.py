from Crypto.Cipher import DES


class Encryption:

    def __init__(self, key_string):
        self.key = key_string
        self.des = DES.new(self.key.encode('utf-8'), DES.MODE_ECB)

    def encrypt(self, text):
        padded_text = pad(text)
        return self.des.encrypt(padded_text.encode('utf-8'))

    def get_des(self):
        return self.des

    def decrypt(self, encrypted_text):
        return self.des.decrypt(encrypted_text)


def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

