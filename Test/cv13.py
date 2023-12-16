# Python program to explain cv2.blur() method 

# importing cv2 
import cv2 

# path 
path = r"C:\Users\yeash\Downloads\OIP.jpeg"

# Reading an image in default mode 
image = cv2.imread(path) 

# Window name in which image is displayed 
window_name = 'Image'

# ksize 
for i in range(60):

    ksize = (2, 2) 

    # Using cv2.blur() method 
    image = cv2.blur(image, ksize, cv2.BORDER_DEFAULT) 

    # Displaying the image 
    cv2.imshow(window_name, image)
    cv2.waitKey(777)
