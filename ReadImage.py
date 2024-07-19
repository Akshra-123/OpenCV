import cv2
image=cv2.imread("C:/Users/akshr/OneDrive/Pictures/MyProfPic.jpg")
image=cv2.imshow("Output",image)
cv2.waitKey(0)
''' cv2.waitKey() is a function from the OpenCV library used to pause the program and wait for the
user to press a key. It’s often used when you display images or videos to control how long the image
 is shown and to capture keyboard events. '''
cv2.destroyAllWindows()
'''
In OpenCV, cv2.destroyAllWindows() is a function used to close all the windows that were
created by cv2.imshow(). It's particularly useful when you want to ensure that all OpenCV
windows are closed after displaying images or videos. '''
