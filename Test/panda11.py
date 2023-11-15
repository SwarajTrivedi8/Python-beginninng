import pandas as pd
import numpy as np
t=pd.read_csv("C:/Users/yeash/Desktop/Book1.csv",dtype={"Salary":np.float64},names=["a","b","c","d"],skiprows=2)           #used for reading the exported excel sheet of extension csv
print(t)