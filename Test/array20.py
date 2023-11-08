import numpy as np

a=np.array([[1,2,3],[3,4,5],[4,5,6]])

print(np.mean(a))
print(np.mean(a,axis=0))
print(np.mean(a,axis=1))