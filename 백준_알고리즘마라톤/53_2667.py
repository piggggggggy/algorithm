# 단지번호붙이기_중

import sys

n = int(sys.stdin.readline())

lst = [[int(j) for j in sys.stdin.readline().strip()] for i in range(n)]

cnt = 0

def apart(a, b):
    global cnt
    if a >= 0 and a < n and b >= 0 and b < n:
        if lst[a][b] == 1:
            lst[a][b] = 2
            cnt +=1
            apart(a-1, b)
            apart(a+1, b)
            apart(a, b-1)
            apart(a, b+1)
        return
    else:
        return

cnt_list = []
for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            apart(i, j)
            cnt_list.append(cnt)
            cnt = 0

cnt_list.sort()
print(len(cnt_list))
for k in cnt_list:
    print(k)

