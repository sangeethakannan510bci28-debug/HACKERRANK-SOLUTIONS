def print_formatted(number):
    # your code goes here
    l1 = int((len((bin(number))[2:])))
    for i in range(1,number+1):
        decimal = str(i)
        octal = str(oct(i))[2:]
        hexadecimal = str(hex(i))[2:].upper()
        binary = str(bin(i))[2:]
        print(f"{decimal:>{l1}} {octal:>{l1}} {hexadecimal:>{l1}} {binary:>{l1}}")

if __name__ == '__main__':
