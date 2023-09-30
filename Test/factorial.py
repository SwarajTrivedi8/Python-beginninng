a=int(input("Enter the no: "))
def fact(n):
     if n==0:
         return 1
     else: 
         return n*fact(n-1)
print("factorial is:",fact(a))

# def add(a,b):
#     return a+b
# print(add(2,3))