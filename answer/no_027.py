import numpy as np
# 27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)
Z = np.arange(10)
print(Z)
#[0 1 2 3 4 5 6 7 8 9]

print(Z**Z)
#[0**0 1**1 2**2 3**3 4**4 ...]

print( 2 << Z >> 2)
# bit shift
# 2 << 0 = 10 10 >> 2 = 0
# 2 << 1 = 100 100 >> 2 = 1
# 2 << 2 = 1000 1000 >> 2 = 10 = 2
# 2 << 3 = 10000 10000 >> 2 = 100 = 4

print(Z < -Z)
# [0<-0 1<-1...]

print(1j*Z)

print(Z/1/1)

#print(Z<Z>Z)