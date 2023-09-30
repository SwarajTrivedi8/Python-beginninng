def coundown(n):
    if n==0:
        print("Blast off")
    else:
        print(n,end=" ")
        coundown(n-1)
coundown(9)