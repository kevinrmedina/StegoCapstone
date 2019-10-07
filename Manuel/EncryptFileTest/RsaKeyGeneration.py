from Crypto.PublicKey import RSA


class RsaKeyGeneration:

    def __index__(self, key_length):
        self.__key_length = key_length
        self.__key = RSA.generate(self.__key_length)

    def generate_public_key(self):
        return self.__key.publickey().exportKey()

    def generate_private_key(self, password):
        return self.__key.exportKey(passphrase=password, pkcs=8, protection="scryptAndAES128-CBC")
