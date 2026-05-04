import numpy
n,m = map(int, input().split())
arr = numpy.array([input().strip().split() for _ in range(n)], int)
print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
out = numpy.std(arr, axis=None)
if  out==0:
    print("{0:.1f}".format(out))
else:
    print("{0:.11f}".format(out))
