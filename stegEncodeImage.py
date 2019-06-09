from LSBSteg.py import *

carrier = LSBSteg(cv2.imread("puppy.png")
payload = carrier.encode_image(cv2.imread("frog.png"))
cv2.imwrite("puppyWithPayload.png", payload)
