# 괄호_중_스택

import sys

n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

for i in data:
    count = 0
    if i[0] == ')' or i[-1] == '(':
        print('NO')
    else:
        for j in i:
            if j == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                break
        if count == 0:
            print('YES')
        else:
            print('NO')