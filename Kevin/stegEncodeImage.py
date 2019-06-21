#!/usr/bin/env python
from LSBSteg import *

#carrier = LSBSteg(cv2.imread("frog.png"))
#payload = carrier.encode_image(cv2.imread("small.jpg"))
#cv2.imwrite("frogWithPayload.png", payload)
steg = LSBSteg(cv2.imread("frog.png"))
data = open("document.docx", "rb").read()
new_img = steg.encode_binary(data)
cv2.imwrite("frogWithPayload.png", new_img)
