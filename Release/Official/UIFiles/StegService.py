#!/usr/bin/env python
from LSBSteg import *

import sys

class StegService():

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