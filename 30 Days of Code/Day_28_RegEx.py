#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input().strip())

    mail_list = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]
        
        emailID = first_multiple_input[1]
        x = re.search("^.*@gmail.com$", emailID)
        
        if x:
            mail_list.append(firstName)
    mail_list.sort()
    for i in mail_list:
        print(i)
