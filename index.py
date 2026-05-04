def minion_game(string):
    # your code goes here
    stuart_score = 0
    kevin_score = 0
    for index, x in enumerate(string):
        if x in "AEIOU":
            kevin_score += len(string) - index
        else:
            stuart_score += len(string) - index
    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")
if __name__ == '__main__':
