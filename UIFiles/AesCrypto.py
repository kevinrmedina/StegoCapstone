from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AesCrypto:

    def __init__(self, key_bytes):
        self.__key = key_bytes
        self.__cipher = AES.new(self.__key, AES.MODE_CBC)
        self.__iv = self.__cipher.iv

    def encrypt(self, plaintext_bytes):
        padded_bytes = pad(plaintext_bytes, AES.block_size)
        return self.__cipher.encrypt(padded_bytes)

    def get_iv(self):
        return self.__iv

    @staticmethod
    def decrypt(encrypted_bytes, key,  iv):
        decrypt_cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        return unpad(decrypt_cipher.decrypt(encrypted_bytes), AES.block_size)
