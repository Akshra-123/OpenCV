import cv2
import numpy as np

img=cv2.imread("C:/Users/akshr/OneDrive/Pictures/MyProfPic.jpg")
img_blur=cv2.GaussianBlur(img,(7,7),0) 
img_canny=cv2.Canny(img,100,100)



hor_img=np.hstack((img,img_blur))
ver_img=np.vstack((img,img))

cv2.imshow("Horizontal Image",hor_img)
cv2.imshow("Vertical Image",ver_img)

cv2.waitKey()
