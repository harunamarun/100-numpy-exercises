import numpy as np
# 43. Make an array immutable (read-only) (★★☆)
Z = np.ones(10)
Z.flags.writeable = False
print(Z)
Z[0] = 5
#ValueError: assignment destination is read-only