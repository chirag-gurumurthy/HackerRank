#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    my_list = []

    while n > 0:
        my_list.append(n % 2)
        n = int(n/2)

    my_list.reverse()
    count = 0
    max_count = 0
    for i in range(len(my_list)):   
        if my_list[i] == 1:
            count += 1
            if count > max_count:
                max_count = count
        elif my_list[i] == 0:
            count = 0
            
    print(max_count) 
