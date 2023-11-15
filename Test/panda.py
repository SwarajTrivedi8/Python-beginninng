import pandas as pd
import numpy as np

data=np.array(["a","b","c","d"])
s=pd.Series(data,index=[100,101,102,103])           #Used for assigning the variable indices to the given data.
print(s)



data=np.array(["Math","Physics","Chemistry","Biology"])
s=pd.Series(data,index=[200,210,220,230])           #Used for assigning the variable indices to the given data.
print(s)