import numpy as np
# 30. How to find common values between two arrays? (★☆☆)
X = np.random.randint(0, 10,10)
Y = np.random.randint(0, 10,10)
print(X)
print(Y)
print(set(X) & set(Y))
print(np.intersect1d(X,Y))