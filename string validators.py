if __name__ == '__main__':
    s = input()
    
    results = [False for i in range(0,5)]

    for i in range(0, len(s)):
        results[0] = results[0] or s[i].isalnum()
        results[1] = results[1] or s[i].isalpha()
        results[2] = results[2] or s[i].isdigit()
        results[3] = results[3] or s[i].islower()
        results[4] = results[4] or s[i].isupper()
    
    for result in results:
        print(result)
