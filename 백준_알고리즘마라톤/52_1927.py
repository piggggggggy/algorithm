# 최소 힙_ 중

import sys, heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    k = int(sys.stdin.readline())
    if k == 0 and len(heap) == 0:
        print(0)
    elif k == 0:
        result = heapq.heappop(heap)
        print(result)
    else:
        heapq.heappush(heap, k)