a=[2,3,64,64]
k=max(a)
l=len(a)
for i in a:
    if k==i:
        a.remove(i)
print(a)