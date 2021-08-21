# 설탕배달_하_기본수학1

N = int(input())
result = 0
lst = []


for i in range(N//5, 0, -1):
    if (N - 5*i) % 3 == 0:
        result = i + (N - 5*i)//3
        lst.append(result)

if N % 3 == 0:
    lst.append(N//3)

_result = 0
if len(lst) == 0:
    _result = -1
else:
    _result = min(lst)

print(_result)


# n = int(input())
# count = 0
#
# while n % 5:
#     n -= 3
#     count += 1
#
#     if 0 < n < 3:
#         print(-1)
#         exit()
#
# print(count + n // 5)
