from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP, AES


class RsaCrypto:

    def __init__(self, private_key, public_key, password):
        self.public_key = RSA.import_key(open(public_key, 'rb').read())
        self.private_key = RSA.import_key(open(private_key, 'rb').read(), passphrase=password)
        self.__cipher_rsa = PKCS1_OAEP.new(self.public_key)
        self.__session_key = get_random_bytes(16)
        self.__cipher_aes = AES.new(self.__session_key, AES.MODE_EAX)
        self.__nonce = self.__cipher_aes.nonce

    def get_session_key(self):
        return self.__cipher_rsa.encrypt(self.__session_key)

    def get_nonce(self):
        return self.__nonce

    def encrypt(self, plaintext_bytes):
        cipher_text, tag = self.__cipher_aes.encrypt_and_digest(plaintext_bytes)
        return cipher_text, tag

    @staticmethod
    def decrypt(private_key, password, enc_session_key, nonce, tag, cipher_text):
        plain_private_key = RSA.import_key(private_key, passphrase=password)
        cipher_rsa = PKCS1_OAEP.new(plain_private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        return cipher_aes.decrypt_and_verify(cipher_text, tag)
