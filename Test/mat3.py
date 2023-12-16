from matplotlib import pyplot as plt
import numpy as np

x=np.arange(0,3*np.pi,.1)
plt.title("WAVES")
y=np.sin(x)
y1=np.cos(x)
plt.subplot(2,1,1)
plt.plot(x,y,"r")
plt.subplot(2,1,2)
plt.plot(x,y1,"g")
plt.show()