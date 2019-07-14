from Crypto.Cipher import DES

key = 'abcdefgh'


def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text


des = DES.new(key.encode('utf-8'), DES.MODE_ECB)
text = 'Python rocks!'
padded_text = pad(text)
encrypted_text = des.encrypt((padded_text.encode('utf-8')))

print(encrypted_text)
print(des.decrypt(encrypted_text))
