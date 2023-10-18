a=["apple","banana","cherry","banana","banana","grape"]
k=[]
j=len(a)
for i in range(j):
    x=a.index("banana",i)
    j=j+x
    k.append(x) 
print(k)