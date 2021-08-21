# 최대 힙_중

# import sys
# n = int(sys.stdin.readline())
# heap = [None]
#
# for i in range(n):
#     k = int(sys.stdin.readline())
#     if k == 0 and len(heap) == 1:
#         print(0)
#     elif k == 0:
#         heap[1], heap[-1] = heap[-1], heap[1]
#         print(heap.pop())
#         m = 1
#         while m <= len(heap)-1:
#             if len(heap)-1 < m*2:
#                 break
#             elif len(heap)-1 == m*2 and heap[m] < heap[m*2]:
#                 heap[m], heap[m*2] = heap[m*2], heap[m]
#                 m = m*2
#             else:
#                 if heap[m*2] > heap[m*2 +1] and heap[m] < heap[m*2]:
#                     heap[m], heap[m*2] = heap[m*2], heap[m]
#                     m = m*2
#                 elif heap[m*2] <= heap[m*2 +1] and heap[m] < heap[m*2+1]:
#                     heap[m], heap[m*2+1] = heap[m*2+1], heap[m]
#                     m = m*2+1
#     else:
#         heap.append(k)
#         if len(heap) > 2:
#             while heap.index(k) > 1:
#                 l = (heap.index(k))//2
#                 if heap[-1] > heap[l]:
#                     heap[-1], heap[l] = heap[l], heap[-1]
#                 else:
#                     break
#


# try2 _ heapq
import sys
import heapq
n = int(sys.stdin.readline())
heap = []

for i in range(n):
    k = int(sys.stdin.readline())
    if k == 0 and len(heap) == 0:
        print(0)
    elif k == 0:
        result = heapq.heappop(heap)
        print(-result)
    else:
        heapq.heappush(heap, -k)
