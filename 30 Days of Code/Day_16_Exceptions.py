#!/bin/python3

import math
import os
import random
import re
import sys




S = input().strip()
try:
    conv = int(S)
    print(conv)
except ValueError:
    print("Bad String") 
