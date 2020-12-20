# Code contributed by Varshini
# install opencv
# install dlib
# install face_recognition
# Part 1


# importing libraries
import cv2
import dlib

# To capture video from webcam
cap = cv2.VideoCapture(0)
# To use video file as input
# cap = cv2.VideoCapture("filename.mp4")

# To detect face
detector = dlib.get_frontal_face_detector()

# To predict 68 landmarks on face
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


while True:
    # Read the frame
    _, frame = cap.read()
    
    # Convert colored image to grayscale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # detect faces in the grayscale image
    faces = detector(gray)
    
    # determine the facial landmarks for the face region
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        landmarks = predictor(gray, face)
        
        # loop over the face detections
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            
            # convert dlib's circle to a OpenCV-style bounding box
	    # then draw the face boundry circle
            cv2.circle(frame, (x, y), 4, (255, 0, 0), -1)
            
    # Display        
    cv2.imshow("Frame", frame)
    
    # Stop if escape key is pressed
    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break
        
# Release the VideoCapture
cap.release()
