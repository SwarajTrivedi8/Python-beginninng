import pandas as pd

data={"One":[1.0,2.0,3.0,"-"],"Two":[1,2,3,4]}
k=pd.DataFrame(data,index=["a","b","c","d"])
print(k["One"])