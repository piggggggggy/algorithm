# 스택_하_스택

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# class stack:
#     def __init__(self):
#         self.head = None
#
#     def push(self, value):
#         newhead = Node(value)
#         newhead.next = self.head
#         self.head = newhead
#
#     def pop(self):
#         if self.empty():
#             return -1
#         deletehead = self.head
#         self.head = self.head.next
#         return deletehead
#
#     def size(self):
#         count = 0
#         while self.data is None:
#             self.head = self.head.next
#             count += 1
#
#     def empty(self):
#         if self.head is None:
#             return 1 or 0
#
#     def top(self):
#         if self.head is None:
#             return -1
#         return self.head.data



import sys

n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

lst = []
def stack(data):
    if data.split()[0] == "push":
        lst.append(data.split()[1])
    elif data.split()[0] == "pop":
        if len(lst) == 0:
            return print(-1)
        else:
            return print(lst.pop())
    elif data.split()[0] == "size":
        return print(len(lst))
    elif data.split()[0] == "empty":
        if len(lst) == 0:
            return print(1)
        else:
            return print(0)
    elif data.split()[0] == "top":
        if len(lst) == 0:
            return print(-1)
        else:
            return print(lst[-1])

for i in data:
    stack(i)

# 백준은 sys를 사용해야 풀리는 문제가 있다