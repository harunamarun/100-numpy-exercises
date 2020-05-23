import numpy as np
# 42. Consider two random array A and B, check if they are equal (★★☆)
X = np.random.randint(0,2,2)
Y = np.random.randint(0,2,2)
print(X,Y)

equal = np.array_equal(X,Y)
# equal = np.allclose(X,Y)
print(equal)
