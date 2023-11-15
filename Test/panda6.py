import pandas as pd
import numpy as np
data={"one":pd.Series(["a","b","c"],index=[10,20,30]),"two":pd.Series(["a","b","c","d"],index=[10,20,30,40]),"three":pd.Series(["a","b","c"],index=[10,20,30])}
n=pd.DataFrame(data)
del n["one"]
print(n)