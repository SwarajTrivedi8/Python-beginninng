import numpy as np
a=np.array([1,2,3,4,5,4,4])
b=np.where(a==4)            #used to find the all indices of array element
print(b)



import numpy as np
k=np.array([1,2,3,4,5,4,4])
l=np.where(k%2==0)
m=np.where(k%2!=0)
print(m)
print(l)