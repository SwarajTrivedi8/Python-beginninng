n=int(input("n: "))
a=0
b=1
s=b
print(a,end=" ")
print(b,end=" ")
while s<=n:
    print(s,end=" ")
    a=b
    b=s
    s=a+b


