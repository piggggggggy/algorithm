# 피보나치 함수_ 중하




# try : 1
import sys

T = int(sys.stdin.readline())

# try : 1

# dict_zero = {
#     0:1,
#     1:0
# }
# dict_one = {
#     0:0,
#     1:1
# }
#
# def fibo(n, zero, one):
#     if n in dict_one or dict_zero:
#         return
#     elif n == 0:
#         zero += 1
#     elif n == 1:
#         one += 1
#     else:
#         fibo(n-1, zero, one)
#         fibo(n+1, zero, one)
#
# for i in range(T):
#     cnt_zero = 0
#     cnt_one = 0
#     k = int(sys.stdin.readline())
#     fibo(k, cnt_zero, cnt_one)
#     dict_zero[k] = cnt_zero
#     dict_one[k] = cnt_one
#     print(dict_zero[k], dict_one[k])


# try 2


zero = [1,0,1]
one = [0,1,1]

def fibo(n):
    if len(zero) < n+1:
        for i in range(len(zero), n+1):
            zero.append(zero[-2]+zero[-1])
            one.append(one[-2]+one[-1])
    return

for j in range(T):
    k = int(sys.stdin.readline())
    fibo(k)
    print(zero[k], one[k])
