from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

# GENERATING RSA KEYS
###########################################################################################
code = 'nooneknows'                                                                       #
key = RSA.generate(2048)                                                                  #
encrypted_key = key.exportKey(passphrase=code, pkcs=8, protection="scryptAndAES128-CBC")  #
with open('rsa_example/my_private_rsa_key.bin', 'wb') as f:                               #
    f.write(encrypted_key)                                                                #
with open('rsa_example/my_rsa_public.pem', 'wb') as f:                                    #
    f.write(key.publickey().exportKey())                                                  #
###########################################################################################

# ENCRYPTING DATA
####################################################################################
with open('rsa_example/encrypted_data.bin', 'wb') as out_file:                     #
    recipient_key = RSA.import_key( open('rsa_example/my_rsa_public.pem').read())  #
    session_key = get_random_bytes(16)                                             #
                                                                                   #
    cipher_rsa = PKCS1_OAEP.new(recipient_key)                                     #
    out_file.write(cipher_rsa.encrypt(session_key))                                #
                                                                                   #
    cipher_aes = AES.new(session_key, AES.MODE_EAX)                                #
    data = b'blah blah blah Python blah blah'                                      #
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)                          #
    out_file.write(cipher_aes.nonce)                                               #
    out_file.write(tag)                                                            #
    out_file.write(ciphertext)                                                     #
####################################################################################

# DECRYPTING & PRINTING DATA
#######################################################################################################
with open('rsa_example/encrypted_data.bin', 'rb') as fobj:                                            #
    private_key = RSA.import_key(open('rsa_example/my_private_rsa_key.bin').read(), passphrase=code)  #
                                                                                                      #
    enc_session_key, nonce, tag, ciphertext = [fobj.read(x)                                           #
                                               for x in (private_key.size_in_bytes(), 16, 16, -1)]    #
    cipher_rsa = PKCS1_OAEP.new(private_key)                                                          #
    session_key = cipher_rsa.decrypt(enc_session_key)                                                 #
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)                                            #
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)                                             #
                                                                                                      #
print(data)                                                                                           #
#######################################################################################################
