#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    list1 = [2, 3, 4, 5]
    list2 = []
    for i in range(6,21):
        list2.append(i)
    if N % 2 != 0:
        print("Weird")
    elif (N % 2 == 0) and (N in list1):
        print("Not Weird")
    elif (N % 2 == 0) and (N in list2):
        print("Weird")
    elif (N % 2 == 0) and (N > 20):
        print("Not Weird")
