#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

totalSwap = 0
while True:
    for i in range(n - 1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            totalSwap += 1
            break
    else:
        break

print('Array is sorted in {} swaps.'.format(totalSwap))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[-1]))
