from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes


class DesKeyGenerator:

    def __init__(self, password):
        self.__password = password
        self.__salt = get_random_bytes(8)

    def generate_key_from_password(self):
        return PBKDF2(self.__password, self.__salt, dkLen=8)

    def get_salt(self):
        return self.__salt

    @staticmethod
    def generate_key_from_predetermined_salt(password, salt):
        return PBKDF2(password, salt, dkLen=8)