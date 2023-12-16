import numpy as np
m=[]
n=0
for i in range(3):
    if n==0:
        STDIN=int(input("ROWS: "))
    if n==1:
        STDIN=int(input("COLUMNS: "))
    if n==2:
        STDIN=int(input("BREATH: "))
    k=m.append(STDIN)
    n=n+1
a=np.zeros(m,dtype=int)
b=np.ones(m,dtype=int)
print(a)
print(b)