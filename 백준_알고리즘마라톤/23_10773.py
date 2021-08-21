# 제로_하_스택

import sys

data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

result_list = []
for i in data:
    if i[0] != 0:
        result_list.append(i[0])
    else:
        result_list.pop()

print(sum(result_list))