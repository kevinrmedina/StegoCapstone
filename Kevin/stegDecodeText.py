from LSBSteg import *

im = cv2.imread("frogWithSecret.png")
steg = LSBSteg(im)
print("Text value:",steg.decode_text())
