c="12345"

for i in range(2,-1,-1):
    x=input("Enter the password: ")
    if x==c:
        print("succesfully logged in")
        break
    else:
        print("invalid,chance remaining",i)
        continue
if x==c:
    print("done")
else:
    print("account locked")