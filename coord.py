if __name__ == '__main__':
    z = complex(input())
    x = z.real
    y = z.imag
    import cmath
    print(abs(complex(x, y)))
    print(cmath.phase(complex(x, y)))
