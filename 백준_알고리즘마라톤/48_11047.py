# 동전0_중

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
lst = deque([])
for i in range(n):
    lst.appendleft(int(sys.stdin.readline()))

cnt = 0
for j in lst:
    if j <= k:
        cnt += k//j
        k = k%j

print(cnt)
