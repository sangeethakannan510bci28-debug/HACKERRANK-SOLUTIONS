from collections import deque

if __name__ == "__main__":
    n = int(input())
    queue = deque()
    op, val = "", 0
    
    for _ in range(n):
        s = input().split()
        if len(s) > 1:
            op, val = s
            eval(f"queue.{op}({val})")
        else:
            op = s[0]
            eval(f"queue.{op}()")
    
    print(" ".join((str(q) for q in queue)))
