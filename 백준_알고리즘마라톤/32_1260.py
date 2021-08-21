# DFS와 BFS_중_DFS와 BFS

import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

root = {i:[] for i in range(1, N+1)}
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    root[a].append(b)
    root[b].append(a)

def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                add = list(set(graph[n])-set(visited))
                add.sort(reverse=True)
                stack += add
    return visited

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                add = list(set(graph[n]) - set(visited))
                add.sort()
                queue += add
    return visited



print(*DFS_with_adj_list(root,V))
print(*BFS_with_adj_list(root,V))


# string_dfs = ''
# string_bfs = ''
# for i in DFS_with_adj_list(root, V):
#     string_dfs += str(i)+' '
# for i in BFS_with_adj_list(root, V):
#     string_bfs += str(i)+' '
#
# print(string_dfs)
# print(string_bfs)