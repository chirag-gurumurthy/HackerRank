# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

T = int(input())
for _ in range(T):
    n = int(input())
    if n > 1:
        sqrt_n = math.sqrt(n)
        for i in range(2, int(sqrt_n)+1):
            if n % i == 0:
                print("Not prime")
                break
        else:
            print("Prime")
    else:
         print("Not prime")
