import numpy as np
# 51. Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)

Z = np.zeros(10, [('position', [('x', float), ('y', float)]),
                  ('color',    [('r', float), ('g', float), ('b', float)])])
print(Z)
