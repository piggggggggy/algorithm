# N-Queen_중_백트래킹
# visited = [1] * N 깊은 복사/얕은 복사

import sys

N = int(sys.stdin.readline())
a, b, c = [False] * N, [False] * (N*2 -1), [False] * (N*2-1)

result = 0
def nqueen(depth, n):
    global result
    if depth == n:
        result += 1
        return

    for k in range(n):
        if not a[k] and not b[depth+k] and not c[depth-k+n-1]:
            a[k] = True
            b[depth+k] = True
            c[depth-k+n-1] = True
            nqueen(depth+1, n)
            a[k] = False
            b[depth + k] = False
            c[depth - k + n - 1] = False

nqueen(0, N)
print(result)