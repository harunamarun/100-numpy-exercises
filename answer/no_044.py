import numpy as np
# 44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)

Z = np.random.rand(10,2)
print(Z)
X = Z[:,0]
Y = Z[:,1]
r = np.sqrt(X*X+Y*Y)
d = np.arctan(Y/X)
print(r)
print(d)

# arctan2 The “four quadrant” arctan of the angle formed by (x, y) and the positive x-axis.
# T = np.arctan2(Y,X)
# print(T)