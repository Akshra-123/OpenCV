import cv2

img=cv2.imread("C:/Users/akshr/OneDrive/Pictures/MyProfPic.jpg")

# canny Image
img_canny=cv2.Canny(img,100,100)
cv2.imshow("CannyImage",img_canny)

cv2.waitKey()