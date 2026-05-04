if __name__ == '__main__':
    N = int(input())
    list_ = []
    for _ in range(N):
        args = []
        command = input().split()
        for x in range(len(command)):
            if x == 0:
                cmd = command[x]
            else:
                args.append(command[x])
        if cmd == "insert":
            list_.insert(int(args[0]),int(args[1]))
        elif cmd == "remove":
            list_.remove(int(args[0]))
        elif cmd == "append":
            list_.append(int(args[0]))
        elif cmd == "sort":
            list_.sort()
        elif cmd == "pop":
            list_.pop()
        elif cmd == "reverse":
            list_.reverse()
        elif cmd == "print":
            print(list_)
        else:
            continue
