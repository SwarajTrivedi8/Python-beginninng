import numpy as np

a=np.ones((5,5),dtype="int")        #used for generating one matrix of given rows and column
b=5*np.ones((5,5),dtype="int")
c=a+b
print(c)