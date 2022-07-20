import cv2

# Load the cascade file
face_cascade = cv2.CascadeClassifier('D:\Python\open cv clg\haarcascade1')

# To capture video from webcam.
video = cv2.VideoCapture(0)

# video.set(3, 1280)
# video.set(4, 720)
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')
font = cv2.FONT_HERSHEY_SIMPLEX

# fontScale
fontScale = 1

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2

while True:
    # Read the frame
    success, img = video.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.2, 6)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        org = (x, y)
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 100, 255), 2)
        cv2.putText(img, 'Face', org, font, fontScale, color, thickness, cv2.LINE_AA)
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    cv2.waitKey(1)


# plus hand detection


