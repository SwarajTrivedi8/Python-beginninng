import pandas as pd

data={"subject":["Eng.math","Physics","chem","Python"],"CA1":[16,18,20,12],"CA2":[27,"-",10,"-"]}
k=pd.DataFrame(data,index=[1,2,3,4])
print(k)