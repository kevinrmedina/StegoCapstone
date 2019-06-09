from LSBSteg import *

carrier = LSBSteg(cv2.imread("puppy.png")
payload = carrier.encode_image(cv2.imread("small.jpg"))
cv2.imwrite("puppyWithPayload.png", payload)

