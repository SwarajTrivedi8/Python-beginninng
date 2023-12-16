import numpy as np
from matplotlib import pyplot as plt

data = [23, 17, 35, 29, 12, 41]
cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR', 'MERCEDES']
plt.pie(data,labels=cars)
plt.legend()
plt.show()