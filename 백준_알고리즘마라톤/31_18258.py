# 큐2_하_큐, 덱

import sys

n = int(sys.stdin.readline())
# data = [sys.stdin.readline().strip() for i in range(n)]
queue_list = []
count = 0
for i in range(n):
    T = sys.stdin.readline().split()
    if T[0] == 'push':
        queue_list.append(T[1])
    elif T[0] == 'pop':
        if len(queue_list)-count == 0:
            print(-1)
        else:
            print(queue_list[0+count])
            count += 1
    elif T[0] == 'size':
        print(len(queue_list)-count)
    elif T[0] == 'empty':
        if len(queue_list)-count == 0:
            print(1)
        else:
            print(0)
    elif T[0] == 'front':
        if len(queue_list)-count == 0:
            print(-1)
        else:
            print(queue_list[0+count])
    elif T[0] == 'back':
        if len(queue_list)-count == 0:
            print(-1)
        else:
            print(queue_list[-1])

# def queue2(text):
#     T = text.split()
#     if T[0] == 'push':
#         queue_list.append(T[1])
#         return
#     elif T[0] == 'pop':
#         if not queue_list:
#             return print(-1)
#         else:
#             return print(queue_list.pop(0))
#     elif T[0] == 'size':
#         return print(len(queue_list))
#     elif T[0] == 'empty':
#         if not queue_list:
#             return print(1)
#         else:
#             return print(0)
#     elif T[0] == 'front':
#         if not queue_list:
#             return print(-1)
#         else:
#             return print(queue_list[0])
#     elif T[0] == 'back':
#         if not queue_list:
#             return print(-1)
#         else:
#             return print(queue_list[-1])
#
# for i in range(n):
#     data = sys.stdin.readline().strip()
#     queue2(data)
#