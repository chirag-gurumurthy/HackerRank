import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    for i in range(n):
        my_list = arr[::-1]
        
        for j in my_list:
            print(j, end=" ")
        break
