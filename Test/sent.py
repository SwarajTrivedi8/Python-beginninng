tup=4,6,7,87,54
lis=list(tup)
o=[]
odd=tuple(o)
e=[]
even=tuple(e)
for i in range(len(lis)-2):
    h=(i*2)
    k=lis[h]
    e.append(k)
for d in range(len(lis)-3):
    s=d*2+1
    j=lis[s]
    o.append(j)
print("Odd:",odd)
print("Even:",even)
