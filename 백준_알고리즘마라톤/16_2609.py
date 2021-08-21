# 최대공약수와 최소공배수_하_정수론 및 조합론
import sys

A, B = map(int, sys.stdin.readline().split())

a_list = []
b_list = []
for k in range(A, 0, -1):
    if A % k == 0:
        a_list.append(k)
for k in range(B, 0, -1):
    if B % k ==0:
        b_list.append(k)

set_a = set(a_list)
set_b = set(b_list)
max_ab = max(set_a & set_b)

a = A//max_ab
b = B//max_ab

min_ab = max_ab * a * b
print(max_ab)
print(min_ab)


#### 정답!

# max_ab = 0
# if A > B:
#     for i in b_list:
#         if i in a_list:
#             max_ab = i
#             break
# else:
#     for i in a_list:
#         if i in b_list:
#             max_ab = i
#             break
# 반복문보다 set이 좋을 때가 있다. 이게 더 느림