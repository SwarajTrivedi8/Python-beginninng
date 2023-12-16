from matplotlib import pyplot as plt
import numpy as np

x=[1,2,3,4,5]
y=[1,4,9,16,25]
y1=[2,8,18,32,50]
plt.plot(x,y,"g",x,y1,"r")
plt.legend("Single element")
plt.show()