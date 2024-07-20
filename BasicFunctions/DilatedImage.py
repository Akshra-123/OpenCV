import cv2
import numpy as np

img=cv2.imread("C:/Users/akshr/OneDrive/Pictures/MyProfPic.jpg")
kernel=np.ones((5,5),np.uint8)

img_canny=cv2.Canny(img,100,100)
img_dialation=cv2.dilate(img_canny,kernel,iterations=1)

cv2.imshow("Dialiated Image",img_dialation)
cv2.waitKey() 

''' In terms of binary image image dilation refers to the increasing width of the white part '''