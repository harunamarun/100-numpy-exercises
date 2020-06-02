import numpy as np
# 64. Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)? (★★★)

# bincount 各要素が何個あるか数えてくれる
Z = np.zeros(5)
I = np.random.randint(0, len(Z), 8)
print(I)
Z += np.bincount(I, minlength=len(Z))
print(np.bincount(I, minlength=len(Z)))
print(Z)

# Another solution
# Author: Bartosz Telenczuk
#np.add.at(Z, I, 1)
#print(Z)
