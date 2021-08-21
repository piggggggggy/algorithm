# k번째 수_중상

import sys
N = int(sys.stdin.readline())
k = int(sys.stdin.readline())


b_list = []
for i in range(1, N+1):
    for j in range(1, N+1):
        num = i*j
        b_list.append(num)
b_list.sort()
print(b_list)
print(b_list[k])

