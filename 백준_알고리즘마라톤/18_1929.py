# 소수 구하기_중하_기본수학2

import sys

M, N = map(int, sys.stdin.readline().split())

n = 1000000
prime_list = [True] * n

m = int(n ** 0.5)

for i in range(2, m+1):
    if prime_list[i]:
        for j in range(i * 2, n, i):
            prime_list[j] = False

prime_list[1] = False

for k in range(M, N+1):
    if prime_list[k]:
        print(k)






















# M, N = map(int, input().split())
#
# prime_list = []
# for l in range(2, M):
#     for m in range(2,l+1):
#         if l%m == 0 and m*m <=l:
#             break
#         else:
#             prime_list.append(l)
# for i in range(M, N+1):
#     if i > 2:
#         for j in prime_list:
#             if i%j == 0 and j*j <=i:
#                 break
#         else:
#             prime_list.append(i)
#             print(i)
#
#     elif i == 2:
#         print(i)