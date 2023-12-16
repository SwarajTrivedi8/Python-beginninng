import numpy as np
from matplotlib import pyplot as plt
x=np.arange(1,10)
plt.title("WAVES")
y=x*x+x+2
y1=x/2
y2=(x*x+2)/4
plt.plot(x,y,"r",x,y1,"g",x,y2,"k")
plt.show()