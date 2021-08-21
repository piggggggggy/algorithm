# 바이러스_중

import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
lst = [[] for i in range(n+1)]

for i in range(m):
    n, m = map(int, sys.stdin.readline().split())
    if m not in lst[n]:
        lst[n].append(m)
    if n not in lst[m]:
        lst[m].append(n)

visit = []
stack = [1]
while stack:
    k = stack.pop()
    if k not in visit:
        visit.append(k)
        for j in lst[k]:
            if j not in visit:
                stack.append(j)

print(len(visit)-1)