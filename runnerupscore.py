if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    first = second = float('-inf')
    for x in arr:
        if(x > first):
            second = first
            first = x            
        elif(x > second and x != first):
            second = x    
