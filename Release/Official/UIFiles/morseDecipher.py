#!/usr/bin/env python3
import sys

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
                    '0':'-----', ' ':'/', '':'', '\"':'.-..-.', '$':'...-..-',
                    '\'':'.----.', '(':'-.--.', ')':'-.--.-', '[':'-.--.',
                    ']':'-.--.-', '+':'.-.-.', ',':'--..--', '-':'-....-', '/':'-..-.',
                    '.':'.-.-.-', ':':'---...', ';':'-.-.-.', '=':'-...-',
                    '?':'..--..', '@':'.--.-.', '_':'..--.-', '!':'---.'}
option = sys.argv[1]
message = sys.argv[2]
if option == '1':
    #message = 'SOS'
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += '/ '
    tempFile = open('/tmp/morseCodeTemp', 'w')
    tempFile.write(cipher)
    tempFile.close()

if option == '2':
    #message = '...'
    decipher = ''
    citext = ''

    for letter in message:
        if (letter != ' '):
            citext += letter

        else:
            decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
            citext = ''
    tempFile = open('/tmp/morseCodeTemp', 'w')
    tempFile.write(decipher)
    tempFile.close()

