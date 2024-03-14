import cv2
import numpy as np

# Read an example image
image = cv2.imread("C:\\Users\\pavit\\Downloads\\cv_projects\\1imag.jpg")
cv2.imshow("Original image",image)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("binary image",binary_image)

# Define a kernel for erosion and dilation
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
erosion_image = cv2.erode(binary_image, kernel, iterations=1)
cv2.imshow("eroded image",erosion_image)

# Apply dilation
dilation_image = cv2.dilate(binary_image, kernel, iterations=1)
cv2.imshow("dilated image" ,dilation_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()