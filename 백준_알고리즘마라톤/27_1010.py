# 다리놓기_중_정수론 및 조합론

import sys

def factorial(k):
    if k == 1 or k == 0:
        return 1
    res = k * factorial(k-1)
    return res


n = int(sys.stdin.readline())
for i in range(n):
    N, M = map(int, sys.stdin.readline().split())
    result = int( factorial(M) / (factorial(N) * factorial(M-N)))
    print(result)







# def bridge(A, l):
#     for k in range(A + 1 - l):
#         bridge(A-l, k)
#         count += 1
#         print('p')
#     return
#
# 조합공식을 활용하면 쉽게 풀수 이쓴 문제
#