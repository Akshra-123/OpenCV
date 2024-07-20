import cv2

video=cv2.VideoCapture("C:/Users/akshr/Videos/Captures/Calculator 2024-05-31 21-23-06.mp4")

while True:
    success,image=video.read()
    cv2.imshow("video",image)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break