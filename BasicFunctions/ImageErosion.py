import cv2
import numpy as np
'''image erosion is the process of thinning the white part that is the opposite of dilation'''

img=cv2.imread("C:/Users/akshr/OneDrive/Pictures/MyProfPic.jpg")
img_canny=cv2.Canny(img,100,100)

kernel=np.ones((5,5),np.uint8)
img_dialation=cv2.dilate(img_canny,kernel,iterations=1)


img_erosion=cv2.erode(img_dialation,kernel,iterations=1)

cv2.imshow("Eroded Image",img_erosion)

cv2.waitKey()
cv2.destroyAllWindows()