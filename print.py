def print_formatted(number):
    for x in range(1, number + 1, 1):
        o = oct(x)[2:]
        h = hex(x)[2:].upper()
        b = bin(x)[2:]
        l = len(bin(number)[2:])
        print(' '.join(f"{val}".rjust(l) for val in (x, o, h, b)))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
