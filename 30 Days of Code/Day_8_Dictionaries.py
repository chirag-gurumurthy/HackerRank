# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n = int(input())

phoneBook = {}

for i in range(n):

    entry = input().strip().split(' ')
       
    phoneBook[entry[0]] = entry[1]

query_name = sys.stdin.readline().strip()

while query_name:
    
    if query_name in phoneBook:
        print(query_name + '=' + phoneBook.get(query_name))
    else:
        print("Not found")  
          
    query_name = sys.stdin.readline().strip()
