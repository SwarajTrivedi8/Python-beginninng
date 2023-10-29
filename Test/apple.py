a={}
for i in "apple":
    a[i]=a.get(i,0)+1
    print(a)
    sorted(a.items())