from Crypto.Hash import MD5
import AesManager
import DesManager


password = 'abcdefgh'
key, salt = AesManager.get_key_and_salt(password, 32)
filepath_out = 'aes_encrypted.bin'
aes_filepath_in = 'aes_plaintext'
AesManager.write_encrypted_text(key, filepath_out, 'hi', salt)
AesManager.write_decrypted_text(password, aes_filepath_in, filepath_out)

des_key = b'abcdefgh'
DesManager.write_encrypted_text(des_key, 'des_encrypted.bin', 'hi')
des_filepath_in = 'des_plaintext'
DesManager.write_decrypted_text(des_key, des_filepath_in, 'des_encrypted.bin')

checksum = MD5.new()
checksum.update(open('hi', 'rb').read())
print(checksum.hexdigest())

checksum = MD5.new()
checksum.update(open(aes_filepath_in, 'rb').read())
print(checksum.hexdigest())

checksum = MD5.new()
checksum.update(open(des_filepath_in, 'rb').read())
print(checksum.hexdigest())
