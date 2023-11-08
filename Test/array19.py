import numpy as np

a=np.array([[0,1,2],[2,3,4],[-9,1,-1]])
b=np.amax(a)    #used for finding the max value in the matrix.
print(b)
c=np.amin(a)
print(c)        #used for findind the minimum value of matrix.

v=np.amax(a,axis=1)     #used for finding the max value of row of matrix.
print(v)

v=np.amin(a,axis=1)     #used for finding the min value of row of matrix.
print(v)

h=np.array([[65,60,30],[1,2,3],[70,69,95]])

f=np.median(h,axis=1)
f=f.astype(int)         #used to transfor datatype of matrix elements.
print(f)