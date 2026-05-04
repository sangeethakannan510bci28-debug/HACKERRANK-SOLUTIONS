# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = r'(?<= )(&&|\|\|)(?= )'
replace = lambda m : 'and' if m.group() == '&&' else 'or'
print(*(re.sub(pattern,replace,input()) for _ in range(int(input()))),sep='\n')
