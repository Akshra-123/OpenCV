import cv2
import numpy as np

img=cv2.imread("C:/Users/akshr/OneDrive/Desktop/cardsImg.jpg")

source_pts=np.float32([[863,292],[1018,529],[636,770],[487,514]])
destination_pts=np.float32([[6,3],[1049,9],[1038,729],[44,729]])

matrix=cv2.getPerspectiveTransform(source_pts,destination_pts)
warped_image=cv2.warpPerspective(img,matrix,(600,700))
cv2.imshow("Image",img)
cv2.imshow("Warped Image",warped_image)
cv2.waitKey()

# Getting the concept but unable to get the right dimensions
