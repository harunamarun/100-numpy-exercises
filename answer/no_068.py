# import pandas as pd
import numpy as np
# 68. Considering a one-dimensional vector D, how to compute means of subsets of D using a vector S of same size describing subset indices? (★★★)
# 68. 1次元ベクトルDを考えると、部分集合インデックスを記述する同じサイズのベクトルSを使用して、Dの部分集合の平均を計算する方法は？

D = np.arange(10)
S = np.random.randint(0, 4, 10)
print(D)
print(S)
D_sums = np.bincount(S, weights=D)
print("D_sums")
print(D_sums)
D_counts = np.bincount(S)
print("D_counts")
print(D_counts)
D_means = D_sums / D_counts
print("D_means")
print(D_means)

# # Pandas solution as a reference due to more intuitive code
# print(pd.Series(D).groupby(S).mean())
