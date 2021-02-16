# Documentation:
# https://docs.opencv.org/master/d6/d00/tutorial_py_root.html

# Install OpenCV in order for the imports to work properly,
# open the terminal on your machine and run the command:
# Mac / Linux users: pip3 install opencv-python
# Windows users: pip install opencv-python
# or hover over the red underlined import and select "install opencv"

# OpenCV import:
import cv2
import numpy as np

# Variables
windowName = "Alphabet Window!"

# Loads Image (stored in the "img" variable)
img = cv2.imread('assets/alphabet.png', -1)
face_img = cv2.imread('assets/face.png', -1)

# Resize Image (To 25% of its original size)
img = cv2.resize(img, (0,0), fx=0.25, fy=0.25)

# Write an image (filename, source)
# cv2.imwrite("new_img", img)

# Displays Image
cv2.imshow(windowName,img)

# Waits an infinite amount of time for a key press
# Once the user presses any key on the keyboard
# all the displayed images will be destroyed / closed
cv2.waitKey(0)
cv2.destroyAllWindows()

