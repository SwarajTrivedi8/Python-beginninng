import pandas as pd
import numpy as np
data={"one":pd.Series([10,20,30],index=["a","b","c"]),"two":pd.Series([10,20,30,40],index=["a","b","c","d"])}
n=pd.DataFrame(data)
k=n.loc["c":"d"]                #used for finding the string in the table
print(k)