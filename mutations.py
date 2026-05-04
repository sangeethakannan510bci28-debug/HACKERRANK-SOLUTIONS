def mutate_string(string, position, character):
    c = string[:position] + character + string[position+1:]
    return c

if __name__ == '__main__':
