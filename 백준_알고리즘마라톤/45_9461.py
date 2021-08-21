# 파도반 수열_중

import sys
T = int(sys.stdin.readline())
lst = [1,1,1,2,2]


for j in range(T):
    n = int(sys.stdin.readline())
    for i in range(len(lst)+1,n+1):
        if n <= 5:
            break
        elif len(lst) < n:
            p = lst[i-2] + lst[i-6]
            lst.append(p)
        else:
            break
    print(lst[n-1])
