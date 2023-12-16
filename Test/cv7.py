import cv2
import numpy as np
for i in range(5):
    i=i+1
    a=i*50*np.ones((400,400,3),dtype="uint8")
    cv2.imshow("bright",a)
    cv2.waitKey(777)