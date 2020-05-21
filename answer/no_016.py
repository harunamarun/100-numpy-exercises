import numpy as np
# 16. How to add a border (filled with 0's) around an existing array? (★☆☆)
Z = np.random.randint(0, 10, (5, 5))

print(np.pad(Z, (1, 1), "constant"))

# Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
# print(Z)