#!/usr/bin/env python
from LSBSteg import *

#steg = LSBSteg(cv2.imread("frogWithPayload.png"))
#orig_im = steg.decode_image()
##cv.SaveImage("recovered.png", orig_im)
#cv2.imwrite("recovered.jpg", orig_im)
steg = LSBSteg(cv2.imread("frogWithPayload.png"))
binary = steg.decode_binary()
file = open("recovered.jpg", "wb")
file.write(binary)
