import numpy as np

a=np.array([6,7,8,9])
b=np.searchsorted(a,7,side="left")          #used to find index of an element with specified side.
print(b)




a=np.array([1,5,7])
b=np.searchsorted(a,[6,4,2])          #used to find index of an element which will be placed between them with specified side.
print(b)