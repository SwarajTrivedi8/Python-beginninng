k=0
def max1(a):
    if a>k:
        print(a)
    else:
        k=a+max1(a)
        