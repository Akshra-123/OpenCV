import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)

cv2.putText(img,"Learning OpenCV",(65,200),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,130,2),2)

cv2.imshow("Image",img)
cv2.waitKey()