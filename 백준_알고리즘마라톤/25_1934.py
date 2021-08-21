# 최소공배수_하_정수론 및 조합론

import sys

n = int(sys.stdin.readline())

for i in range(n):
    A, B = map(int, sys.stdin.readline().split())
    a_list = []
    b_list = []
    for k in range(1, int(A**0.5)+1):
        if A % k == 0:
            a_list.append(k)
            if k !=(A//k):
                a_list.append(A//k)
    for k in range(1, int(B**0.5)+1):
        if B % k ==0:
            b_list.append(k)
            if k !=(B//k):
                b_list.append(B//k)

    set_a = set(a_list)
    set_b = set(b_list)
    max_ab = max(set_a & set_b)
    a = A//max_ab
    b = B//max_ab
    min_ab = max_ab * a * b
    print(min_ab)

# 시간초과였지만 약수를 N의 반으로 나누어 구하는 방법을 적용해 성공


# import sys
#
# n = int(sys.stdin.readline())
# for i in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#
#     if a < b:  # make a bigger
#         a, b = b, a

#     num1 = a
#     num2 = b
#
#     while num1 % num2 != 0:
#         div = num1 % num2
#
#         num1 = num2
#         num2 = div
#
#     biggest_divisor = num2
#
#     print(biggest_divisor * a // biggest_divisor * b // biggest_divisor)
#
# 알아보고 싶은 방법