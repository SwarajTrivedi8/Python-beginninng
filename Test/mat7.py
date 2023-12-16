import numpy as np
import matplotlib.pyplot as plt
y=np.array([35,25,25,15])
mylabels=["apples","banana","cherries","dates"]
plt.pie(y,labels=mylabels)
plt.show()