class car():
    def __init__(self,name):
        print("Product is:",name)
    def calc(self,x,y):
        return x*y
item1=car("Lambo")
item1.name="Lambo"
item1.price=400000
item1.quantity=3
print(item1.calc(item1.price,item1.quantity))


item2=car("Bucatti")
item2.name="Bucatti"
item2.price=400000
item2.quantity=4
print(item2.calc(item2.price,item2.quantity))