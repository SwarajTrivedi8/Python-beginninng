import pandas as pd

a=pd.DataFrame([[1,2],[3,4]],columns=["a","b"])
b=pd.DataFrame([[5,6],[7,8]],columns=["c","d"])
c=a._append(b)
k=c.drop(0)                     #used to delete the rows of same name which is given
print(k)