import cv2
import numpy as np

# Create a black image (all zeros) with dimensions 500x500 and 3 channels (RGB)
image = np.zeros((500, 500, 3))

# Draw a blue rectangle
cv2.rectangle(image, (50, 50), (200, 150), (255, 0, 0), -1)  # -1 for filling the rectangle

# Draw a green circle
cv2.circle(image, (300, 300), 50, (0, 255, 0), -1)  # -1 for filling the circle

# Draw a red line
cv2.line(image, (350, 100), (450, 200), (0, 0, 255), 2)  # 2 is the thickness of the line

# Display the image
cv2.imshow("colorful 2D objects", image)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
