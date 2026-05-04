import numpy
a1 = numpy.array(input().strip().split(), int)
a2 = numpy.array(input().strip().split(), int)
print(numpy.inner(a1,a2), numpy.outer(a1,a2), sep='\n')
