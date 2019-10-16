from Crypto.PublicKey import RSA


class RsaKeyGenerator:

    def __init__(self):
        self.key = RSA.generate(2048)

    def generate_public_key(self):
        return self.key.publickey().export_key()

    def generate_private_key(self, password):
        return self.key.exportKey(passphrase=password, pkcs=8, protection="scryptAndAES128-CBC")