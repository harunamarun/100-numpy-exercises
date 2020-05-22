import numpy as np
# 31. How to ignore all numpy warnings (not recommended)? (★☆☆)

Z = np.ones(1) / 0
print(Z)
defaults = np.seterr(all="ignore")
print(Z)

# Suicide mode on
# defaults = np.seterr(all="ignore")
# Z = np.ones(1) / 0

# # Back to sanity
# _ = np.seterr(**defaults)

# # Equivalently with a context manager
# nz = np.nonzero([1,2,0,0,4,0])
# print(nz)