import pandas as pd

a=[["pen",20],["pencil",10],["eraser",5],["colors",50]]
k=pd.DataFrame(a,columns=["object","price"])
m=k.to_csv("C:/Users/yeash/Desktop/Book1.csv")
