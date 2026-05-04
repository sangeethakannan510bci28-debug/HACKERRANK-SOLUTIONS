# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
pattern = r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])'
matches = re.findall(pattern, s)

if matches:
    print(*matches, sep='\n')
else:
    print(-1)
