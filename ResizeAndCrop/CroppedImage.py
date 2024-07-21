import cv2
import numpy as np

img=cv2.imread("C:/Users/akshr/OneDrive/Pictures/MyProfPic.jpg")
print(img.shape)

croppedImage=img[0:400,200:400]

cv2.imshow("Cropped Image",croppedImage)
cv2.waitKey()