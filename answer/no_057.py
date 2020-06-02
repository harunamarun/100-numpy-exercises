import numpy as np
# 57. How to randomly place p elements in a 2D array? (★★☆)
Z = np.zeros((10,10))
print(Z)
print(np.put(Z,np.random.choice(100,10),1))
print(Z)
