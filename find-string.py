def count_substring(string, sub_string):
    s = len(sub_string)
    count = 0
    result = [string[x : x + s] for x in range(len(string) - (s-1))]
    for i in result:
        if i == sub_string:
            count += 1
    return count


if __name__ == '__main__':
