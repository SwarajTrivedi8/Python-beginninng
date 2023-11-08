import numpy as np

a=[[1,2,3],[5,7,9]]
b=[4,5,6]

k=np.array(a)
v=np.array(b)
print(v)
c=np.add(k,v)
print(c)
print("     ")
j=np.multiply(k,v)
print(j)
print("     ")
s=np.divide(k,v)
print(s)
print("     ")
g=np.dot(k,v)
print(g)