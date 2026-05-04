# Enter your code here. Read input from STDIN. Print output to STDOUTimport math
import math

AB = int(input())
BC = int(input())

print(f"{round(math.degrees(math.atan(AB/BC)))}\u00b0")
