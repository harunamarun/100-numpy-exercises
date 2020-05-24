import numpy as np
# 48. Print the minimum and maximum representable value for each numpy scalar type (★★☆)
I = [np.int8, np.int16, np.int32, np.int64]
F = [np.float16, np.float32, np.float64, np.float128]

for i in I:
    print(np.iinfo(i).max, np.iinfo(i).min)
for f in F:
    print(np.finfo(f).max, np.finfo(f).min)
    #print(np.finfo(f).eps)


#　eps: machine epsilon