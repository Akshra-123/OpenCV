import cv2
import numpy as np

# Open a connection to the camera
cap = cv2.VideoCapture(0)

# Set the frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open video capture")
else:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()   # ret is a boolean variable that indicates 
                                   # whether the frame was successfully from the video stream.
        # If frame is read correctly ret is True
        if not ret:
            print("Error: Can't receive frame (stream end?). Exiting ...")
            break

        # Display the resulting frame
        cv2.imshow('Frame', frame)
        
        
        brightness=50
        bright_frame=cv2.add(frame,np.array([brightness]))

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    cap.release()

    # Destroy all OpenCV windows
    cv2.destroyAllWindows()


    cv2.waitKey(1)