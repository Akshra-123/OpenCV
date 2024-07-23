import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)

# To colour the image
img[:]=255,0,0

# if want to colour a specific part of image
# img[200:300,300:500]=255,0,0

# Creating a line over image
cv2.line(img,(00,00),(512,512),(0,255,0),6)
'''(image,starting point,ending point,colour code,thickness)''' 

# Creating Rectangle
cv2.rectangle(img,(100,100),(250,350),(0,0,255),3)

# Filling the rectangle
cv2.rectangle(img,(0,0),(50,50),(0,230,0),cv2.FILLED)

# Circle 
cv2.circle(img,(450,50),40,(255,255,0),6)
cv2.imshow("Image",img)
cv2.waitKey()
