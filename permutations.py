if __name__ == '__main__':
    S, k = input().split()
    k = int(k)
    from itertools import permutations
    l = sorted(list(permutations(S, k)))
    for x in l:
        print(''.join(x))
