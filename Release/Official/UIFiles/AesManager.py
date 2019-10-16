from AesCrypto import AesCrypto
from AesKeyGeneration import AesKeyGenerator


def write_encrypted_text(key, out_filename, plaintext_filename, salt):
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


def get_key_and_salt(password, key_length):
    generator = AesKeyGenerator(password, key_length)
    return generator.generate_key_from_password(), generator.get_salt()
