# -*- coding:utf-8 -*-
# list1 = [2, 6, 3, 5, 1, 8]
# print(list1)
# list1.append(0)
# print(list1)
# c2 = list1.insert(2, 0)
# print(list1)
# print(c2)

# def jie(n):
#     if n == 1:
#         return 1
#     else:
#         return n * jie(n - 1)
#
#
# print(jie(3))

# import matplotlib.pyplot as plt
#
# fight = (3, 2, 1, 101, 99, 98, 10)
# kiss = (105, 100, 81, 10, 5, 2, 90)
# filmType = (1, 1, 1, 2, 2, 2, 3)
# plt.scatter(fight, kiss, c=filmType)
# plt.show()

import numpy as np
import knn as K
import matplotlib.pyplot as plt

fight = [3, 2, 1, 101, 99, 98]
kiss = [104, 100, 81, 10, 5, 2]
filmType = [1, 1, 1, 2, 2, 2]
# plt.scatter(fight, kiss, c=filmType)
# plt.xlabel("fight")
# plt.ylabel("kiss")
# plt.title("movie")
# plt.show()

x = np.array([fight, kiss])
x = x.T
print(x)
y = np.array(filmType)
print(y)

xx = np.array([18, 90])
result = K.knn(xx, x, y, 4)
print("result:", result)
