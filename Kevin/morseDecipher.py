#!/usr/bin/env python3

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..',
                    'E':'.', 'F':'..-.',
                    'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---',
                    'K':'-.-', 'L':'.-..',
                    'M':'--', 'N':'-.', 'O':'---',
                    'P':'.--.', 'Q':'--.-', 'R':'.-.',
                    'S':'...', 'T':'-', 'U':'..-', 'V':'...-',
                    'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----',
                    '2':'..---', '3':'...--', '4':'....-', '5':'.....',
                    '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ':'/', '':''}

def encrypt(message):
    #message = 'SOS'
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += '/'
    return cipher

def decrypt(message):
    #message = '...'
    decipher = ''
    citext = ''

    for letter in message:
        if (letter != ' '):
            citext += letter

        else:
            decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
            citext = ''
    return decipher
    #print decipher

