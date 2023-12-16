import numpy as np
N=int(input())
A=list(map(int,input().split(" ")))
B=list(map(int,input().split(" ")))

A1=np.array([A])
B1=np.array([B])

c=np.cross(A1,B1)
print(c)