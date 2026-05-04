# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
A = defaultdict(list)
[A[input()].append(i) for i in range(1, n + 1)]
[print(*(A.get(input(), [-1]))) for _ in range(m)]
