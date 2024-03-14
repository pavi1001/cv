import cv2
frameWidth = 640
frameHeight = 480

# Load the pre-trained face detection model
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Open a video capture object
cap = cv2.VideoCapture("10th.jpg")
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 130)

while True:
    success, img = cap.read()

    if not success:
        break

    imgResize = cv2.resize(img, (500, 400))
    imgGray = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = faceCascade.detectMultiScale(imgResize, 1.1, 4)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(imgResize, (x, y), (x + w, y + h), (255, 0, 0), 1)

    # Display the processed image
    cv2.imshow("img",imgResize)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
