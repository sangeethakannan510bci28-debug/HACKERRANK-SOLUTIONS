#!/bin/python3

import math
import os
import random
import re
import sys


def countOccurences(listInput, value):
    num = 0
    for i in listInput:
        if value == i:
            num += 1
    return num

def getDistinctValues(listInput):
    distinctValues = []
    for i in listInput:
        if i not in distinctValues:
            distinctValues.append(i)
    return distinctValues


if __name__ == '__main__':
    s = input()
    distinctValues = getDistinctValues(list(s))
    
    for i in range(0, len(distinctValues)):
        distinctValues[i] = [distinctValues[i], countOccurences(s, distinctValues[i])]
    
    distinctValues = sorted(distinctValues, key = lambda x: (-x[1], x[0]))
    print(str(distinctValues[0][0]) + " " + str(distinctValues[0][1]))
    print(str(distinctValues[1][0]) + " " + str(distinctValues[1][1]))
    print(str(distinctValues[2][0]) + " " + str(distinctValues[2][1]))

