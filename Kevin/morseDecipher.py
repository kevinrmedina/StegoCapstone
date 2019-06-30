#!/usr/bin/env python

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..',
                    'E':'.', 'F':'..-.',
                    'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---',
                    'K':'-.-', 'L':'.-..'}

def decrypt():
    message = '.- -... -.. '

    decipher = ' '
    citext = ''

    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter

        else:
            i += 1

            if i == 2 :
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''

    print decipher

decrypt()
