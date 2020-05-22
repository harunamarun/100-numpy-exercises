import numpy as np
# 22. Normalize a 5x5 random matrix (★☆☆)
Z = np.random.rand(5, 5)
print((Z - Z.mean()) / Z.std())
