import numpy
n,m,p = map(int, input().split())
arr1 = numpy.array([input().strip().split() for _ in range(n+m)], int)
print(arr1)
