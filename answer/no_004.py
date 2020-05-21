import numpy as np
# 4. How to find the memory size of any array (★☆☆)
Z = np.zeros((4, 4))
print("{} bytes".format(Z.size * Z.itemsize))
#print("%d bytes" % (Z.size * Z.itemsize))