# 6. Convert an image from one color space to another.

import cv2

# Load an image
image = cv2.imread('C:\\Users\\pavit\\Downloads\\cv_projects\\1imag.jpg')

# Convert the image from BGR (default in OpenCV) to RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert the image from RGB to Grayscale
gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)

# Display the original, RGB, and Grayscale images
cv2.imshow('Original Image', image)
cv2.imshow('RGB Image', rgb_image)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()