from LSBSteg import *

steg = LSBSteg(cv2.imread("frog.png"))
img_encoded = steg.encode_text("Just gonna add some text here.")
cv2.imwrite("frogWithSecret.png", img_encoded)
