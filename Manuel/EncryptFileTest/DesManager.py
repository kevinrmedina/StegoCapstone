from DesCrypto import DesCrypto
from DesKeyGeneration import DesKeyGenerator


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
