#
# import cv2
# from cvzone.HandTrackingModule import HandDetector
#
#
#
# cap = cv2.VideoCapture(0)
# detector = HandDetector(detectionCon=0.8, maxHands=2)
#
# while True:
#     success, img = cap.read()
#     hands, img = detector.findHands(img)  # With Draw
#     # hands = detector.findHands(img, draw=False)  # No Draw
#
#     if hands:
#         # Hand 1
#         hand1 = hands[0]
#         lmList1 = hand1["lmList"]  # List of 21 Landmarks points
#         bbox1 = hand1["bbox"]  # Bounding Box info x,y,w,h
#         centerPoint1 = hand1["center"]  # center of the hand cx,cy
#         handType1 = hand1["type"]  # Hand Type Left or Right
#
#         # print(len(lmList1),lmList1)
#         # print(bbox1)
#         # print(centerPoint1)
#         fingers1 = detector.fingersUp(hand1)
#         # length, info, img = detector.findDistance(lmList1[8], lmList1[12], img) # with draw
#         # length, info = detector.findDistance(lmList1[8], lmList1[12])  # no draw
#
#
#         if len(hands) == 2:
#             hand2 = hands[1]
#             lmList2 = hand2["lmList"]  # List of 21 Landmarks points
#             bbox2 = hand2["bbox"]  # Bounding Box info x,y,w,h
#             centerPoint2 = hand2["center"]  # center of the hand cx,cy
#             handType2 = hand2["type"]  # Hand Type Left or Right
#
#             fingers2 = detector.fingersUp(hand2)
#             # print(fingers1, fingers2)
#             # length, info, img = detector.findDistance(lmList1[8], lmList2[8], img) # with draw
#             length, info, img = detector.findDistance(centerPoint1, centerPoint2, img)  # with draw
#
#     cv2.imshow("Image", img)
#     cv2.waitKey(1)

import cv2
from cvzone.HandTrackingModule import HandDetector


# Load the cascade file
face_cascade = cv2.CascadeClassifier('D:\Python\open cv clg\haarcascade1')

# To capture video from webcam.
video = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8, maxHands=4)

# video.set(3, 1280)
# video.set(4, 720)
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')
font = cv2.FONT_HERSHEY_COMPLEX
# org
# fontScale
fontScale = 1.3
# Blue color in BGR
color = (0, 0, 255)
# Line thickness of 2 px
thickness = 1
while True:
    # Read the frame
    success, img = video.read()
    detector.findHands(img)
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.2, 6)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        org = (x, y)
        cv2.rectangle(img, (x, y), (x+w, y+h), (144, 220, 144), 3)
        cv2.putText(img, 'basith', org, font, fontScale, color, thickness, cv2.LINE_AA)
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    cv2.waitKey(1)


