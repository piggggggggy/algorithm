# 색종이만들기_중_분할정복

import sys
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

print(data)
# [[1, 1, 0, 0, 0, 0, 1, 1],
#  [1, 1, 0, 0, 0, 0, 1, 1],
#  [0, 0, 0, 0, 1, 1, 0, 0],
#  [0, 0, 0, 0, 1, 1, 0, 0],
#  [1, 0, 0, 0, 1, 1, 1, 1],
#  [0, 1, 0, 0, 1, 1, 1, 1],
#  [0, 0, 1, 1, 1, 1, 1, 1],
#  [0, 0, 1, 1, 1, 1, 1, 1]]


one_count = 0
zero_count = 0

def cut_paper(N, graph_list):
    global one_count, zero_count
    sum_cnt = 0

    for i in range(int(N)):
        cell = graph_list[i]
        sum_cnt += sum(cell)

    if sum_cnt == N**2:
        one_count += 1
        return
    elif sum_cnt == 0:
        zero_count += 1
        return
    else:
        new_list_1 = []
        new_list_2 = []
        new_list_3 = []
        new_list_4 = []
        cnt = 0
        for j in graph_list:
            if cnt < N/2:
                left = j[:int(N/2)]
                right = j[int(N/2):]
                new_list_1.append(left)
                new_list_2.append(right)
            else:
                left = j[:int(N/2)]
                right = j[int(N/2):]
                new_list_3.append(left)
                new_list_4.append(right)
            cnt +=1

        cut_paper(N/2, new_list_1)
        cut_paper(N/2, new_list_2)
        cut_paper(N/2, new_list_3)
        cut_paper(N/2, new_list_4)

cut_paper(n, data)

print(zero_count)
print(one_count)

