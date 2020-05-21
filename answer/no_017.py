import numpy as np
# 17. What is the result of the following expression? (★☆☆)
print(0 * np.nan) 
# nan
print(np.nan == np.nan)
# False
print(np.inf > np.nan)
# False
print(np.nan - np.nan)
# nan
print(np.nan in set([np.nan]))
# True
print(0.3 == 3 * 0.1)
# False