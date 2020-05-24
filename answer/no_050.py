import numpy as np
# 50. How to find the closest value (to a given scalar) in a vector? (★★☆)

Z = np.arange(10)
print(Z)
print(Z-5.5)
print(Z[np.argmin(np.abs(Z-5.5))])
