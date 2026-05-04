if __name__ == '__main__':
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    from itertools import product
    C = list(product(A, B))
    C.sort()
    for x in C:
        print(x, end = ' ')
    print("\n")
