import pandas as pd

data1={"Name":["Sanjeev","Keshav","Rahul"],"Age":["37","42","38"],"Designation":["Manager","Clerk","Accountant"]}
mat=pd.DataFrame(data1)
sort=mat.sort_values(by=["Age"])
print(sort.to_string(index=False))