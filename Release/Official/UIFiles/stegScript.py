#!/usr/bin/env python
from LSBSteg import *

import sys

def encodeFile(cF, pF, nF):
    carrier = LSBSteg(cv2.imread(cF))
    payload = open(pf, "rb").read()
    result = carrier.encode_binary(payload)
    cv2.imwrite(nF, result)
    return;

def decodeFile(cF, nF):
    carrier = LSBSteg(cv2.imread(cF))
    binaryExtract = carrier.decode_binary()
    newFile = open(nF, "wb")
    newFile.write(binaryExtract)
    return;

def encodeText(cF, nF, text):
    carrier = LSBSteg(cv2.imread(cF))
    newFile = carrier.encode_text(text)
    cv2.imwrite(nF, newFile)
    return;

def decodeText(cF):
    carrier = cv2.imread(cF)
    textExtract = LSBSteg(carrier).decode_text()
    print(textExtract)
    return textExtract;

#Add more to help print out
def help():
    print """
    Script options:
    -e: Encode
    -d: Decode
    -t: Text
    -f: File
    """
def main():
#If first argument is zero then it's encoding
    if (sys.argv[1]) == '-e':
        #If second argument is zero then it's for file
        if sys.argv[2] == '-f':
            cF = sys.argv[3]
            pF = sys.argv[4]
            nF = sys.argv[5]
            encodeFile(cF, pF, nF)
        #If second argument is one then it's for text
        elif sys.argv[2] == '-t':
            cF = sys.argv[3]
            nF = sys.argv[4]
            text = sys.argv[5]
            encodeText(cF, nF, text)
    #If first argument is zero then it's encoding
    elif sys.argv[1] == '-d':
        #If second argument is zero then it's for file
        if sys.argv[2] == '-f':
            cF = sys.argv[3]
            nF = sys.argv[4]
            decodeFile(cF, nF)
        #If second argument is one then it's for text
        elif sys.argv[2] == '-t':
            cF = sys.argv[3]
            decodeText(cF)
    elif sys.argv[1] == '-h':
        help()

if __name__ == '__main__':
    main()
