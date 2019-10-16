from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes


class AesKeyGenerator:

    def __init__(self, password, key_length):
        self.__salt = get_random_bytes(key_length)
        self.__password = password

    def generate_key_from_password(self):
        return PBKDF2(self.__password, self.__salt, dkLen=32)

    def get_salt(self):
        return self.__salt

    @staticmethod
    def generate_key_with_predefined_salt(password, salt):
        return PBKDF2(password, salt, dkLen=32)
