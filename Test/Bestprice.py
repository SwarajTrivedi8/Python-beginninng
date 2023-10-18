n=int(input("Enter the no of products: "))
k=[]
for i in range(n):
    p=int(input("Enter the product-"))
    k.append(p)
l=max(k)
g=min(k)
z=k.index(l)
s=k.index(g)
print("The",z+1,"product of price",l,"is high priced")
print("The",s+1,"product of price",g,"is low priced")