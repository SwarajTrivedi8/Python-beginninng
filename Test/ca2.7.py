import cv2
import numpy as np

a=np.zeros((800,400,3),dtype="uint8")

cv2.circle(a,(200,110),100,(0,255,0),10)
cv2.line(a,(200,220),(200,250),(0,255,255),10)
cv2.rectangle(a,(100,250),(300,500),(0,255,255),5)
cv2.line(a,(300,250),(500,250),(0,255,255),5)
cv2.line(a,(100,250),(0,250),(0,255,255),5)
cv2.line(a,(150,500),(150,650),(0,255,255),5)
cv2.line(a,(250,500),(250,650),(0,255,255),5)





font=cv2.FONT_HERSHEY_SIMPLEX
cv2.imshow("dark img",a)


cv2.waitKey()