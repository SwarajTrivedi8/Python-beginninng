import pandas as pd

data=[["rahul",10],["sahil",25],["Reetu",20]]

t=pd.DataFrame(data,columns=["Name","Age"],index=[100,101,102])
t1=t.sort_values(by="Name",ascending=False)                     #Used for sorting the values as columns.
print(t1)