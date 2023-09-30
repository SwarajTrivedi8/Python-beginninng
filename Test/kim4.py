def mod(i):
    if i==0:
        return 1
    else:
        return i*mod(i-1)
mod(4)
mod(9)