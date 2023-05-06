# -*- coding:utf-8 -*-
import numpy as np


def knn(inX, dataSet, labels, k):
    dist = (((dataSet - inX) ** 2).sum(1)) ** 0.5
    sortedDist = dist.argsort()
    classCount = {}
    for i in range(k):
        voteLabel = labels[sortedDist[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    maxType = 0
    maxCount = -1
    for key, value in classCount.items():
        if value > maxCount:
            maxType = key
            maxCount = value
    return maxType
