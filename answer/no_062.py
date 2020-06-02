import numpy as np
# 62. Considering two arrays with shape (1,3) and (3,1),
# how to compute their sum using an iterator? (★★☆)


# np.nditer
A = np.array([[1, 2, 3]])
B = np.array([[4], [5], [6]])
it = np.nditer([A, B])
for x, y in it:
    print("x y:", x, y)

# x y: 1 4
# x y: 2 4
# x y: 3 4
# x y: 1 5
# x y: 2 5
# x y: 3 5
# x y: 1 6
# x y: 2 6
# x y: 3 6


it = np.nditer([A, B, None])
for x, y, z in it:
    z[...] = x + y
    print("x y z:", x, y, z)
print(it.operands[2])
