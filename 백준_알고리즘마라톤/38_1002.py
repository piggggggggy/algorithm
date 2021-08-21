# 터렛_중_기본수학

import sys

n = int(sys.stdin.readline())
for i in range(n):
    points = list(map(int, sys.stdin.readline().split()))
    self_r = ((points[0] - points[3])**2 + (points[1]-points[4])**2)**0.5
    a = points[2]
    b = points[5]
    if self_r == 0:
        if a == b:
            print(-1)
        else:
            print(0)
    else:
        r = a + b
        if a <= self_r and b <= self_r:
            if r < self_r:
                print(0)
            elif r == self_r:
                print(1)
            else:
                print(2)
        else:
            if a == b + self_r or b == a + self_r:
                print(1)
            elif a > b + self_r or b > a + self_r:
                print(0)
            else:
                print(2)
