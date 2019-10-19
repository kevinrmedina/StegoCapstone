import os
from UIFiles.DesCrypto import DesCrypto
from UIFiles.DesKeyGeneration import DesKeyGenerator

def write_encrypted_text(password, out_filename, plaintext_filename):
    generator = DesKeyGenerator(password)
    key = generator.generate_key_from_password()
    salt = generator.get_salt()
    cipher = DesCrypto(key)
    file_in = open(plaintext_filename, 'rb')
    plaintext = file_in.read()
    file_in.close()
    file_out = open(out_filename, 'wb')
    file_out.write(salt)
    file_out.write(cipher.encrypt(plaintext))
    file_out.close()


def write_decrypted_text(password, out_filename, encrypted_filename):
    file_in = open(encrypted_filename, 'rb')
    salt = file_in.read(8)
    file_in.seek(8)
    cipher_text = file_in.read()
    file_in.close()
    file_out = open(out_filename, 'wb')
    key = DesKeyGenerator.generate_key_from_predetermined_salt(password, salt)
    cipher = DesCrypto(key)
    file_out.write(cipher.decrypt(cipher_text, key))
    file_out.close()

def write_encrypted_string(password, plainText):
    generator = DesKeyGenerator(password)
    key = generator.generate_key_from_password()
    salt = generator.get_salt()
    cipher = DesCrypto(key)
    plainTextInBytes = bytes(plainText, 'utf-8')
    cipherText = salt + cipher.get_iv() + cipher.encrypt(plainTextInBytes)
    return cipherText

def write_decrypted_string(password, cipherText):
    file_in = open("tempFile", 'wb')
    file_in.write(cipherText)
    file_in.close()
    file_out = open("tempFile", 'rb')
    salt = file_out.read(8)
    file_in.seek(8)
    cipher_text = file_out.read()
    file_out.close()
    key = DesKeyGenerator.generate_key_from_predetermined_salt(password, salt)
    cipher = DesCrypto(key)
    plainTextInBytes = cipher.decrypt(cipher_text, key)
    plainText = plainTextInBytes.decode('ascii')
    os.remove("tempFile")
    return plaintext
