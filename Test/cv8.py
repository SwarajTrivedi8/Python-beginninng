import cv2
import numpy as np

a=np.zeros((400,400,3),dtype="uint8")
cv2.line(a,(20,20),(150,150),(0,255,255),10)
cv2.imshow("dark img",a)

b=np.zeros((400,400,3),dtype="uint8")
cv2.line(b,(20,20),(150,150),(0,255,255),10)
cv2.imshow("dark img",b)

cv2.waitKey()