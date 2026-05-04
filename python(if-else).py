
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    is_odd = n % 2 == 1
    is_weird = 5 < n < 21
    print(result := "Weird" if is_odd or is_weird else "Not Weird")