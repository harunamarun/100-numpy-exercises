import numpy as np
# 66. Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors (★★★)

w, h = 4, 4
Z = np.random.randint(0, 2, (h, w, 3)).astype(np.ubyte)
F = Z[..., 0]*(256*256) + Z[..., 1]*256 + Z[..., 2]
print(F)
n = len(np.unique(F))
print(n)
print(np.unique(Z))

# print(Z[:,:,0]) and print(Z[...,0]) are same meaning
