import numpy as np
# 46. Create a structured array with x and y coordinates covering the [0,1]x[0,1] area (★★☆)
# xax = np.linspace(0,1,5)
# yax = np.linspace(0,1,5)
# X, Y = np.meshgrid(xax,yax)
# Z = []
# for x, y in zip(X, Y):
#     for xx, yy in zip(x, y):
#         print(xx, yy)

Z = np.zeros((5,5), [('x',float),('y',float)])
Z['x'], Z['y'] = np.meshgrid(np.linspace(0,1,5),np.linspace(0,1,5))
print(Z)