import re
s = ""
for i in range(int(input())):
    s = input()
    m = re.findall(r'(#[a-fA-F0-9]{6}(?=[^\s])|#[a-fA-F0-9]{3}(?=[^\s]))\b', s)
    if m:
        print(*m, sep='\n')
