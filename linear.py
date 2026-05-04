import numpy
n = int(input())
arr = numpy.array([input().strip().split() for i in range(n)], float)
numpy.set_printoptions(legacy='1.13')
print(numpy.linalg.det(arr))
