from Crypto.Hash import MD5
import AesManager
import DesManager
import RsaManager
from RsaKeyGeneration import RsaKeyGenerator
from RsaCrypto import RsaCrypto
import sys

# password = 'abcdefgh'
# key, salt = AesManager.get_key_and_salt(password, 32)
# print()
# filepath_out = 'aes_encrypted.bin'
# aes_filepath_in = 'aes_plaintext'
# AesManager.write_encrypted_text(key, filepath_out, 'hi', salt)
# AesManager.write_decrypted_text(password, aes_filepath_in, filepath_out)
#
# des_key = b'abcdefgh'
# DesManager.write_encrypted_text(des_key, 'des_encrypted.bin', 'hi')
# des_filepath_in = 'des_plaintext'
# DesManager.write_decrypted_text(des_key, des_filepath_in, 'des_encrypted.bin')
#
# checksum = MD5.new()
# checksum.update(open('hi', 'rb').read())
# print(checksum.hexdigest())
#
# checksum = MD5.new()
# checksum.update(open(aes_filepath_in, 'rb').read())
# print(checksum.hexdigest())
#
# checksum = MD5.new()
# checksum.update(open(des_filepath_in, 'rb').read())
# print(checksum.hexdigest())

# password = 'abcdefgh'
# cipher_text_filename = 'des_encrypted.bin'
# deciphered_text_filename = 'des_plaintext'
#
# DesManager.write_encrypted_text(password, cipher_text_filename, 'hi')
# DesManager.write_decrypted_text(password, deciphered_text_filename, cipher_text_filename)
#
# checksum = MD5.new()
# checksum.update(open(deciphered_text_filename, 'rb').read())
# print(checksum.digest())
#
# checksum = MD5.new()
# checksum.update(open('hi', 'rb').read())
# print(checksum.digest())

# generator = RsaKeyGenerator()
# public_key = generator.generate_public_key()
# public_key_file = 'public.key'
# open(public_key_file, 'wb').write(public_key)
#
# password = 'abcdefgh'
# private_key = generator.generate_private_key(password)
# private_key_path = 'private.key'
# open(private_key_path, 'wb').write(private_key)
#
# RsaManager.write_encrypted_stream(public_key_file, 'rsa_encrypted.bin', 'hi')
# RsaManager.write_decrypted_stream(private_key_path, 'rsa_plaintext', 'rsa_encrypted.bin', password)

# in_file_name = 'hi'
# plaintext_in = open(in_file_name, 'rb').read()
#
# public_key = open('public.key', 'rb').read()
# private_key = open('private.key', 'rb').read()
#
# cipher = RsaCrypto(public_key)
# session_key = cipher.get_session_key()
# nonce = cipher.get_nonce()
# cipher_text, tag = cipher.encrypt(plaintext_in)
#
# open('session_key', 'wb').write(session_key)
#
# print(RsaCrypto.decrypt(private_key, 'abcdefgh', session_key, nonce, tag, cipher_text))

public_key = open('public.key', 'rb').read()
private_key = open('private.key', 'rb').read()

cipher_text_filename = 'rsa_encrypted.bin'

plaintext_in = open('hi', 'rb').read()
cipher, tag = RsaManager.write_encrypted_stream(public_key, cipher_text_filename, 'hi')

password = 'abcdefgh'
print('Direct nonce is ' + str(cipher.get_nonce()))
print(cipher.get_session_key())
print('Direct tag is ' + str(tag))
RsaManager.write_decrypted_stream(password, private_key, 'rsa_plaintext', cipher_text_filename)




