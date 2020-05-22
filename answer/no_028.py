import numpy as np
# 28. What are the result of the following expressions?
print(np.array(0))
print(np.array(0) / np.array(0))
# NaN

print(np.array(0) // np.array(0))
# 0
print(np.array([np.nan]).astype(int).astype(float))
