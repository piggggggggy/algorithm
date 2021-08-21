# 블랙잭_중_브루트포스

import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
result_list = []

for i in lst:
    if i <= M:
        for j in lst:
            if j + i <= M and j != i:
                for k in lst:
                    if k + j + i <= M and j != k != i:
                        result_list.append(k+j+i)
print(max(result_list))
