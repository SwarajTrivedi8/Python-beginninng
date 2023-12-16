import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,2*np.pi,0.1)
y=np.sin(x)
plt.subplot(2,1,1)
plt.plot(x,y,"g")
plt.title("sine wave")
y1=np.cos(x)
plt.subplot(2,1,2)
plt.plot(x,y1)
plt.title("cos wave")
plt.tight_layout(pad=3)
plt.show()