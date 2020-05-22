import numpy as np
# 35. How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)
A = np.ones(3)*1
B = np.ones(3)*2

print( np.add(A,B,out=B)) 
# B = A + B
print( np.divide(A,2,out= A))
# A = A / 2
print( np.negative(A,out= A))
# A = -A
print( np.multiply(A,B,out=A))
# A = A * B
print(A)