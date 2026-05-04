if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        a, b = input().split()
        
        try:
            print(int(a)//int(b))
        except ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")
        except ValueError as e:
            print("Error Code:",e)