import numpy as np

a=np.array([[13,79,18],[23,21,24]])
b=np.sort(a)
b1=np.flip(b,axis=1)
print(b1)