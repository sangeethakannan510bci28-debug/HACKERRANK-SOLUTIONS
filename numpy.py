import numpy

if __name__ == "__main__":
    x = tuple(map(int,input().split()))
    zeros_arr = numpy.zeros(x,int)
    ones_arr = numpy.ones(x,int)
    print(zeros_arr, ones_arr, sep="\n
