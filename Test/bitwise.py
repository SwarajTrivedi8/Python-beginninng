a=int(input("Enter the no: "))
if(a%5==0 and a%2==0):
    print (a,"is divisible by 5 and 2")
elif(a%5==0):
    print(a,"is divisible by 5")
elif(a%2==0):
    print(a,"is divisible by 2")
else:
    print(a,"not any of them")