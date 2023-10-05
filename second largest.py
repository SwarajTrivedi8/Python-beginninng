a=[]
n=int(input("Enter the no og elements: "))
for i in range(n):
    k=int(input("Enter the elements: "))
    a.append(k)
b=set(a)
m=max(b)
d=b.remove(m)
l=max(b)
print(l)