#from RsaCrypto import RsaCrypto
import UIFiles.RsaCrypto

def write_encrypted_stream(public_key, out_filename, in_filename):
    cipher = RsaCrypto(public_key)
    session_key = cipher.get_session_key()
    print(session_key)
    nonce = cipher.get_nonce()
    in_file = open(in_filename, 'rb')
    plaintext_in = in_file.read()
    in_file.close()
    cipher_text, tag = cipher.encrypt(plaintext_in)
    out_file = open(out_filename, 'wb')
    out_file.write(session_key)
    out_file.write(nonce)
    out_file.write(tag)
    out_file.write(cipher_text)
    out_file.close()
    return cipher, tag


def write_decrypted_stream(password, private_key, out_filename, cipher_text_filename):
    cipher_text_file = open(cipher_text_filename, 'rb')
    session_key = cipher_text_file.read(256)
    cipher_text_file.seek(256)
    nonce = cipher_text_file.read(16)
    cipher_text_file.seek(32)
    tag = cipher_text_file.read(16)
    cipher_text_file.seek(48)
    cipher_text = cipher_text_file.read()
    cipher_text_file.close()
    print('Extracted session key is ' + str(session_key))
    #print('Extracted nonce is ' + str(nonce))
    #print('Extracted tag is ' + str(tag))
    #print(cipher_text)
    plaintext = RsaCrypto.decrypt(private_key, password, session_key, nonce, tag, cipher_text)
    out_file = open(out_filename, 'wb')
    out_file.write(plaintext)
    out_file.close()


