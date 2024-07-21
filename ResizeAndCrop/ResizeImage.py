import cv2
import numpy

img=cv2.imread("C:/Users/akshr/OneDrive/Pictures/MyProfPic.jpg")
print(img.shape)  
''' when output comes there are three values first shows height , 
second shows width and third shows the colour size i.e RGB '''
ResizeImage=cv2.resize(img,(224,225))

cv2.imshow("Image",img)
cv2.imshow("Resized Image",ResizeImage)
cv2.waitKey()
