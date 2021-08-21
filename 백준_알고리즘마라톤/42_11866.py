# 요세푸스 문제 0_중


import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())

lst = [i+1 for i in range(N)]
yose_list = deque(lst)
result = []

def yose(list, k):
    while len(list) > 0:
        if len(list) == 1:
            result.append(list.pop())
        else:
            for j in range(k-1):
                list.append(list.popleft())
            n = list.popleft()
            result.append(n)
    return result

yose(yose_list, K)
result = ', '.join(map(str, result))
print('<'+result+'>')

