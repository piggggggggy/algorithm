# 오큰수

# 크기가 N인 수열 A = A1, A2, ..., AN이 있다.
# 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
# Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다.
# 그러한 수가 없는 경우에 오큰수는 -1이다.
#
# 예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다.
# A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.


from collections import deque
import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
result = [-1] * n   # [-1, -1, -1,,,,] 만들기

for i in range(n-1):  # result의 마지막은 무조건 -1이 되어야하기 때문에 n-1 까지만
    target_num = lst[i]
    for k in range(i+1, n):
        if target_num < lst[k]:
            result[i] = lst[k]
            break

print(*result)
# -------------------------------- 정답코드

# stack = []
# stack.append(0)
# for i in range(1, n):
#     while stack and lst[stack[-1]] < lst[i]:
#         result[stack.pop()] = lst[i]
#     stack.append(i)
#
# print(*result)
