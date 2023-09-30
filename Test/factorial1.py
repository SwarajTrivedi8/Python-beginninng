def deil(n):
    if n==0:
        print("deleted")
    else:
        print(n)
        deil(n-1)
deil(10)