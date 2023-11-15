import pandas as pd

data=[["alex",10,12,14],["bob",12,21,43],["Clarke",13,22,43]]
t=pd.DataFrame(data,columns=["Name","Age","CA1","CA2"])
t["Sum"]=t["CA1"]+t["CA2"]
k=t.to_csv("C:/Users/yeash/Desktop/Book2.csv")   
n=pd.read_csv("C:/Users/yeash/Desktop/Book2.csv")
print(n)           #used to write the data in the excel sheet.
                                                            #can also be manupulated.