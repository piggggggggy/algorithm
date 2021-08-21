# 회전하는큐_중상_큐

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

index_list = [i+1 for i in range(N)]
dq = deque(index_list)

#  [1,2,3,4,5,6,7,8,9,10]

count = 0
for j in data:
    if dq.index(j) <= len(dq) - dq.index(j):
        while True:
            k = dq.popleft()
            if k == j:
                break
            dq.append(k)
            count += 1
    else:
        while True:
            k = dq.pop()
            count += 1
            if k == j:
                break
            dq.appendleft(k)
print(count)