#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    list1 = [2, 3, 4, 5]
    list2 = []
    for i in range(6,21):
        list2.append(i)
    if n % 2 != 0:
        print("Weird")
    elif (n % 2 == 0) and (n in list1):
        print("Not Weird")
    elif (n % 2 == 0) and (n in list2):
        print("Weird")
    elif (n % 2 == 0) and (n > 20):
        print("Not Weird")
