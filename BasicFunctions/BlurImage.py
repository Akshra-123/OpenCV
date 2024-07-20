import cv2

img=cv2.imread("C:/Users/akshr/OneDrive/Pictures/MyProfPic.jpg")

# for blurring the image
img_blur=cv2.GaussianBlur(img,(7,7),0) 

''' (7,7) specifies the gaussian kernel size here which can be a combination of any odd values
the more the size of kernel the more blur image will be displayed and in place of 0 there can be 
any +ve value which will decide the extent of blurness but if equal to 0 then the blurness will 
be based on the kernel size '''
cv2.imshow("GrayImage",img_blur)

cv2.waitKey()