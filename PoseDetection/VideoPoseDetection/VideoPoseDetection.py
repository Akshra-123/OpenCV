import math
import cv2 
from time import time
import matplotlib.pyplot as plt
import mediapipe as mp
import numpy as np
# Initialising the media pipe pose class
mp_pose=mp.solutions.pose
# Performing on Real Time Videos
# Setting pose detection for videos
pose_video=mp_pose.Pose(static_image_mode=False,min_detection_confidence=0.5,model_complexity=1)
# Initialise the video capture object to read from webcam
# video=cv2.VideoCapture(0)
# Create named window for resizing purpose
cv2.namedWindow('Pose Detection',cv2.WINDOW_NORMAL)
# Initialise video capture object to read image from the system
video=cv2.VideoCapture("E:/OpenCV/PoseDetection/PushUps.mp4")

# Set video camera size 
video.set(3,1280) # for width
video.set(4,960)  # for height
# Initialise a variable to store the time of previous frame
time1=0
# To find out how many frames per second (FPS) your video or camera is capturing.
# Iterate until video is accessed successfully
while video.isOpened():
  # Read a frame
  ok,frame=video.read()
  if not ok:
    continue  
  

# ok is a boolean variable indicating whether the frame is successfully read or not

# Flip the frame horizontally for natural visualisation
  frame=cv2.flip(frame,1)

# Get the width and height of the frame 
  frame_height,frame_width,_=frame.shape
  
  mp_drawing=mp.solutions.drawing_utils

  def detectPose(image,pose,display=True):
    image_rep=image.copy()
    image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    results=pose.process(image_rgb)
    height,width,_=image_rgb.shape
    landmarks=[]


    if results.pose_landmarks:
      mp_drawing.draw_landmarks(image=image_rep,landmark_list=results.pose_landmarks,connections=mp_pose.POSE_CONNECTIONS)
      for landmark in results.pose_landmarks.landmark:
        landmarks.append((int(landmark.x*width),int(landmark.y*height),(landmark.z*width)))
    if display:
      # Display the original input image and the resultant image
      plt.figure(figsize=[22,22])
      plt.subplot(121);plt.imshow(image[:,:,::-1]);plt.title("Original Image");plt.axis('off');
      plt.subplot(122);plt.imshow(image_rep[:,:,::-1]);plt.title("Output Image");plt.axis('off');

      mp_drawing.plot_landmarks(results.pose_world_landmarks,mp_pose.POSE_CONNECTIONS)
    else:
      return image_rep,landmarks
      
  # Perform pose landmark detection
  frame_rep,_=detectPose(frame,pose_video,display=False)

# Process for calculating the FPS(frames per second)
# Calculate the FPS
  time2=time()

# Check if the difference between the previous and this frame from time>0 to avoid division by 0
  if (time1-time2) > 0:
  # calculate no of frames per second
    frames_per_second= 1.0 / (time2 - time1)
  # Write calculated no of frames per second on the frame
    cv2.putText(frame_rep,'FPS: {}'.format(int(frames_per_second)),(10,30),cv2.FONT_HERSHEY,2,(0,255,0),3)

# Update the previous frame time to this frame time as this frame with become previous in this iteration 
  time1=time2

# Display the frame
  cv2.imshow('Pose Detection',frame_rep)

# Wait until a key is pressed
# retreive the ASCII value of the key pressed
  k=cv2.waitKey(1) & 0xFF

# Check if escape is pressed
  if (k==27):
      break

# Release the video capture object
video.release()

# Close all windows
cv2.destroyAllWindows()


