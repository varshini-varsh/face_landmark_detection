# face_landmark_detection
Facial Landmarks Detection
==================
Steps to find 68 points facial landmarks using OpenCV :
 
1. First read image frame from the frame using webcam
2. Converts a video into frames.
3. Find faces from frame using face detector object
4. Find facial landmarks on faces using 'shape_predictor_68_face_landmarks.dat'


## **Requirements: (with versions i tested on)**
 * python          (3.6)
 * opencv          (3.2.0.8)
 * dlib            (19.8.1)
 * face_recognition(1.3.0)
 * cmake           (3.18.4)
 
68 coordinates are detected for the given face by the face detector. The image is shown below.
![Face landmarks coordinates image](facial_landmarks_68.jpg)


## **Applications of Facial Keypoint Detection**
There are several interesting applications of keypoint detection in human faces. A few of them are listed below.

## **Facial feature detection improves face recognition**
Facial landmarks can be used to align facial images to a mean face shape, so that after alignment the location of facial landmarks in all images is approximately the same. Intuitively it makes sense that facial recognition algorithms trained with aligned images would perform much better, and this intuition has been confirmed by many research papers.

## **Head pose estimation**
Once a few landmark points, can estimate the pose of the head. In other words,can figure out how the head is oriented in space, or where the person is looking. E.g. CLM-Framework described in this post also returns the head pose.

## **Face Morphing**
Facial landmarks can be used to align faces that can then be morphed to produce in-between images. An example is shown in Figure 1.

## **Virtual Makeover**
The detected landmarks were used to the calculate contours of the mouth, eyes etc. to render makeup virtually.

## **Landmark detection for virtual makeover.** 
## **Face Replacement**
If you have facial feature points estimated on two faces, you can align one face to the other, and then seamlessly clone one face onto the other.
You can also do something goofy like this............................
