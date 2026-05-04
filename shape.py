import numpy
ar = map(int, input().split())
arr = list(ar)
a1 = numpy.array([arr], int)
print(a1.reshape(3,3))
