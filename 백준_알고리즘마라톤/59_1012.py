# 유기농배추_중상

import sys
sys.setrecursionlimit(99999)
T = int(sys.stdin.readline())

def lettuce(x,y):
    if x >= 0 and x < M and y >= 0 and y < N:
        if lst[y][x] == 1:
            lst[y][x] = 2
            lettuce(x+1, y)
            lettuce(x-1, y)
            lettuce(x, y+1)
            lettuce(x, y-1)

for m in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    lst = [[0] * M for i in range(N)]
    for j in range(K):
        a, b = map(int, sys.stdin.readline().split())
        lst[b][a] = 1

    cnt = 0
    for i in range(M):
        for j in range(N):
            if lst[j][i] == 1:
                lettuce(i,j)
                cnt += 1
    print(cnt)