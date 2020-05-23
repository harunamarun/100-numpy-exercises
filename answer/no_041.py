import numpy as np
# 41. How to sum a small array faster than np.sum? (★★☆)
Z = np.arange(1,6)
print(np.add.reduce(Z))