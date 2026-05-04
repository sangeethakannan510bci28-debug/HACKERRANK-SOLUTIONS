from itertools import product
K, M = map(int,input().split())
print(max(sum(i)%M for i in list(product(*[[x**2 for x in list(map(int, input().split()))[1:]] for _ in range(K)]))))
