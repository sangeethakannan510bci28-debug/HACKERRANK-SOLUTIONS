cube = lambda x: x*x*x

def fibonacci(n):
    fib = [0,1]
    for _ in range(n):
        fib.append(fib[-1]+fib[-2])
    return fib[:-2]
        

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
