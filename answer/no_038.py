import numpy as np
# 38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆)
def generate():
    for x in range(10):
        yield x

Z = np.fromiter(generate(),dtype=float,count=-1)
print(Z)