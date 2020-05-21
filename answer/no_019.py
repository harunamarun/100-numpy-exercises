import numpy as np
# 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
Z = np.ones((8,8))
Z[::2, ::2] = 0
Z[1::2, 1::2] = 0
print(Z)

# Z = np.zeros((8,8),dtype=int)
# Z[1::2,::2] = 1
# Z[::2,1::2] = 1
# print(Z)