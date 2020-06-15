import numpy as np
# 89. How to get the n largest values of an array (★★★)
'''
hint: np.argsort | np.argpartition
INPUT:

OUTPUT:


'''
n = 5
Z = np.arange(10)
A = Z.flatten()
A = np.sort(A)[::-1]
print(A[:n][::-1])


# np.random.shuffle(Z)
# # Slow
# print (Z[np.argsort(Z)[-n:]])

# # Fast
# print (Z[np.argpartition(-Z,n)[:n]])