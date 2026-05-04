# Enter your code here. Read input from STDIN. Print output to STDOUTS = input()

string = input().strip()
lowercase = [i for i in string if i in [i for i in 'abcdefghijklmnopqrstuvwxyz']]
uppercase = [i for i in string if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
odds = [i for i in string if i in '13579']
evens = [i for i in string if i in '02468']

letters = sorted(lowercase) + sorted(uppercase)
numbers = sorted(odds) + sorted(evens)

final_list = letters+numbers

print(''.join(final_list)
