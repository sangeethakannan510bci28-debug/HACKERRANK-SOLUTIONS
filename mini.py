import numpy
n,m = map(int, input().split())
arr = numpy.array([input().strip().split() for _ in range(n)], int)
a_min = numpy.min(arr, axis=1)
print(max(a_min))
