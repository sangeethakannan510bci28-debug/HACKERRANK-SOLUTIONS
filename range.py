from collections import namedtuple

if __name__ == "__main__":
    n = int(input())
    columns = input().split()
    student = namedtuple('student',columns)   

    all_marks = 0
    
    for i in range(n):
        line = input().split()
        current_student = student(*line)
        all_marks += int(current_student.MARKS)
    
    print(round(all_marks/n,2))
