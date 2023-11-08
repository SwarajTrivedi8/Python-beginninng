a="1 w   3g"
c=a.count(" ")
s=a.split()
m=[]

for i in s:
    if i==int or len(i)==2:
        m.append(i)
    else:
        k=i.title()
        m.append(k)
j=" ".join(m)
print(j)