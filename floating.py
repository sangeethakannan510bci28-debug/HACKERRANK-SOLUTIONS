# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for _ in range(n):       # ^[+-.]?\d*[.]?\d+.$
    print(bool(re.search(r"^[+-.]?\d*[.]+\d+$",input())))
    #print(bool(re.search(r"^[+-.]?\d+[.]?\d+$",input())))
