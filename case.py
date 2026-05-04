def swap_case(s):
    swap = []
    string_list = list(s)
    for i in string_list:
        if i.isupper():
            swap.append(i.lower())
        elif i.islower():
            swap.append(i.upper())
        else:
            swap.append(i)
    return "".join(swap)
