import os
from UIFiles.AesKeyGeneration import AesKeyGenerator
from UIFiles.AesCrypto import AesCrypto


def write_encrypted_text(password, out_filename, plaintext_filename):
    generator = AesKeyGenerator(password)
    salt = generator.get_salt()
    key = generator.generate_key_from_password()
    cipher = AesCrypto(key)
    file_in = open(plaintext_filename, 'rb')
    plaintext = file_in.read()
    file_in.close()
    file_out = open(out_filename, 'wb')
    file_out.write(salt)
    file_out.write(cipher.get_iv())
    file_out.write(cipher.encrypt(plaintext))
    file_out.close()


def write_decrypted_text(password, plaintext_filename, encrypted_filename):
    file_in = open(encrypted_filename, 'rb')
    salt = file_in.read(32)
    file_in.seek(32)
    iv = file_in.read(16)
    file_in.seek(48)
    cipher_text = file_in.read()
    file_in.close()
    key = AesKeyGenerator.generate_key_with_predefined_salt(password, salt)
    cipher = AesCrypto(key)
    plaintext = cipher.decrypt(cipher_text, key, iv)
    file_out = open(plaintext_filename, 'wb')
    file_out.write(plaintext)
    file_out.close()

def write_encrypted_string(password, plainText):
    generator = AesKeyGenerator(password)
    salt = generator.get_salt()
    key = generator.generate_key_from_password()
    cipher = AesCrypto(key)
    plainTextInBytes = bytes(plainText, 'utf-8')
    cipherText = salt + cipher.get_iv() + cipher.encrypt(plainTextInBytes)
    return cipherText

def write_decrypted_string(password, cipherText):
    #cipherTextInBytes = bytes(cipherText, 'utf-8')
    file_in = open("tempFile", 'wb')
    file_in.write(cipherText)
    file_in.close()
    file_out = open("tempFile", "rb")
    salt = file_out.read(32)
    file_out.seek(32)
    iv = file_out.read(16)
    file_out.seek(48)
    actualCipherText = file_out.read()
    file_out.close()
    key = AesKeyGenerator.generate_key_with_predefined_salt(password, salt)
    cipher = AesCrypto(key)
    plaintextBytes = cipher.decrypt(actualCipherText, key, iv)
    plaintext = plaintextBytes.decode('ascii')
    os.remove("tempFile")
    return plaintext
    
