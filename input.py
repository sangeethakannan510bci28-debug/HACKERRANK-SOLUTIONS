if __name__ == "__main__":
    x, k = map(int,input().split())
    p = input()
    print(eval(p,{'x':x}) == k)
