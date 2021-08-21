# 정수 삼각형_ 중
import sys

N = int(sys.stdin.readline())

lst = [list(map(int, sys.stdin.readline().split())) for i in range(N)]


# try1 : dfs _ 시간초과

# out = [7]
# result = 0
#
# def pyramid(depth, n, k):
#     global result
#     if depth == n:
#         if result <= sum(out):
#             result = sum(out)
#         return
#
#     for j in range(k,k+2):
#         out.append(lst[depth][j])
#         pyramid(depth+1, n, j)
#         out.pop()
#
# pyramid(1, N, 0)
#
# print(result)

# try2 : dfs _ 시간초과

# out = 7
# result = 0
#
# def pyramid(depth, n, k):
#     global result
#     global out
#     if depth == n:
#         if result <= out:
#             result = out
#         return
#
#     for j in range(k,k+2):
#         out += lst[depth][j]
#         pyramid(depth+1, n, j)
#         out -= lst[depth][j]
#
# pyramid(1, N, 0)
#
# print(result)

# try3


idx = 0
for i in range(n):


