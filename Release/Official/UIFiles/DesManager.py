from UIFiles.DesCrypto import DesCrypto


def write_encrypted_text(key, out_filename, plaintext_filename):
    cipher = DesCrypto(key)
    file_in = open(plaintext_filename, 'rb')
    plaintext = file_in.read()
    file_in.close()
    file_out = open(out_filename, 'wb')
    file_out.write(cipher.encrypt(plaintext))
    file_out.close()


def write_decrypted_text(key, out_filename, encrypted_filename):
    file_in = open(encrypted_filename, 'rb')
    cipher_text = file_in.read()
    file_in.close()
    file_out = open(out_filename, 'wb')
    cipher = DesCrypto(key)
    file_out.write(cipher.decrypt(cipher_text, key))
    file_out.close()
