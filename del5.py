a=[2,3,64,64]
k=max(a)
l=len(a)
for i in range(l+1):
    x=a[i]
    if k==x:
        a.remove(i)
print(a)