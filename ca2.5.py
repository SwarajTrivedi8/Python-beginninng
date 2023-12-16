import numpy as np
from matplotlib import pyplot as plt

plt.title("Curves")
x=np.arange(-5,5)
y1 = 5*x-2
y2 = 5*x^2+2
y3 = 3*x^3
plt.plot(x,y1,"r",x,y2,"g",x,y3,"k")
plt.legend("y")
plt.show()