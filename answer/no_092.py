import numpy as np
import time
# 92. Consider a large vector Z,
#  compute Z to the power of 3 using 3 different methods (★★★)
'''
hint: np.power, *, np.einsum

'''

x = np.random.rand(100000000)
print(x)
print("===")

cur = time.time()
print(np.power(x, 3))
print(time.time() - cur)

cur = time.time()
print(x**3)
print(time.time() - cur)

cur = time.time()
print(np.einsum('i,i,i->i', x, x, x))
print(time.time() - cur)
