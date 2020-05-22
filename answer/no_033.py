import numpy as np
# 33. How to get the dates of yesterday, today and tomorrow? (★☆☆)
t = np.datetime64("Today","D")
y = t - np.timedelta64(1,"D")
tm = t + np.timedelta64(1,"D")

print(t,y,tm)