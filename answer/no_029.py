import numpy as np
# 29. How to round away from zero a float array ? (★☆☆)
Z = np.random.uniform(-10,+10,10)
print(np.where( Z >= 0, np.ceil(Z),np.floor(Z)))


#print (np.copysign(np.ceil(np.abs(Z)), Z))