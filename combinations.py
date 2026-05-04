from itertools import combinations

if __name__ == "__main__":
    s, k = input().split()
    
    for i in range(1,int(k)+1):
        result = combinations(sorted(s),i)
        for x in result:
            print("".join(x))
