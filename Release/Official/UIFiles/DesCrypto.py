from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


class DesCrypto:

    def __init__(self, key):
        self.__key = key
        self.__cipher = DES.new(self.__key, DES.MODE_ECB)

    def encrypt(self, stream):
        padded_stream = pad(stream, DES.block_size)
        return self.__cipher.encrypt(padded_stream)

    def get_cipher(self):
        return self.__cipher

    @staticmethod
    def decrypt(encrypted_text, key):
        decrypt_cypher = DES.new(key, DES.MODE_ECB)
        return unpad(decrypt_cypher.decrypt(encrypted_text), DES.block_size)
