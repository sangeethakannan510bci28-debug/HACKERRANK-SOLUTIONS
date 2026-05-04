from collections import OrderedDict

if __name__ == "__main__":
    n = int(input())
    prices_ord_dict = OrderedDict()
    
    for _ in range(n):
        elem = input().rsplit(" ", 1)
        if prices_ord_dict.get(elem[0]):
            prices_ord_dict[elem[0]] += int(elem[1])
        else:
            prices_ord_dict[elem[0]] = int(elem[1])
    
    for name, price in prices_ord_dict.items():
        print(name, price)
