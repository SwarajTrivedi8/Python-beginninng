import pandas as pd

data={"One":pd.Series([1,2,3],index=["a","b","c"]),"Two":pd.Series([1,2,3,4],index=["a","b","c","d"])}              #Another way to create a data table.
t=pd.DataFrame(data)
t["three"]=[10,20,30,"NaN"]
t["Four"]=t["One"]+t["three"]
print(t)
