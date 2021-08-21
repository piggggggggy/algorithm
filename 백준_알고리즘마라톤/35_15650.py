# N과 M(2)_중_백트래킹

import sys

N, M = map(int, sys.stdin.readline().split())
visited = [False] * N
out = []

def backtracking(depth, n, m):
    if depth == m:
        print(*out)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            backtracking(depth+1, n, m)
            out.pop()

            for j in range(i+1, n):
                visited[j] = False
backtracking(0, N, M)

# def two(depth, idx, n, m):
#     if depth == m:
#         print(*out)
#         return
#
#     for i in (idx, n):   # 달라진 부분
#         out.append(i+1)
#         two(depth, i, n, m)
#         out.pop()
#
        # 이렇게 풀면 visited를 만들지 않아도 되고 매우 간단히 풀 수 잇따..