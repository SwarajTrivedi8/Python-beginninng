import numpy as np
N=list(map(int,input().split(" ")))
M=list(map(int,input().split(" ")))

a=np.array([N,M])
s=np.sum(a,axis=1)
p=np.prod(s,axis=0)
print(p)