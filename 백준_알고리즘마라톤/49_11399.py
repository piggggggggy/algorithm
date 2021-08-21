# ATM_중

import sys
n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

sum = 0
result = 0
for i in lst:
    sum += i
    result += sum

print(result)