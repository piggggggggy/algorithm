# 분해합_중_브루트포스

import sys

N = int(sys.stdin.readline())

def create(n):
    k = int(n)
    for i in str(n):
        k += int(i)
    return k

cnt = 0
while True:
    if create(cnt) == N:
        print(cnt)
        break
    elif cnt == N:
        print(0)
        break
    cnt += 1
