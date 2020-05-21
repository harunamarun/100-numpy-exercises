import numpy as np
# 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
print(np.unravel_index(99, (6, 7, 8)))