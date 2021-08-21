# Fly me to the Alpha Centauri_하_기본수학1

T = int(input())
# memo = {}

def odd_(x):
    result = 0
    count = 0
    while result != x:
        count += 1
        result += count * 2 - 1
        print(result, count)
    return count
    # if x > 0:
    #     result = 2x-1 + odd_(x-1)
    # else:
    #     break
    # return result

def even_(x):
    result = 0
    count = 0
    while result != x:
        count += 1
        result += count * 2
        print(result, count)
    return count
    # if x > 0:
    #     result = 2x-1 + even_(x-1)
    # else:
    #     break
    # return result

for i in range(T):
    x, y = map(int, input().split())
    n = y-x
    if n % 2 == 1:
        num = odd_(n)
    else:
        num = even_(n)
    print(num)





# 1               1   1
# 11              2   2
# 121             4   3
# 1221            6   4
# 12321           9   5
# 123321          12  6
# 1234321         16  7
# 12344321        20  8
# 123454321       25  9
# 1234554321      30  10
# 12345654321     36  11


# 1       1             1       1
# 2       11            2       1
# 3       111           3       2
# 4       121           3       2
# 5       1211          4       2
# 6       1221          4       2
# 7       12211         5       3
# 8       12221         5       3
# 9       12321         5       3
# 10      122221        6       3
# 11      123221        6       3
# 12      123321        6       3
# 13      1123321       7       4
# 14      1223321       7       4
# 15      1233321       7       4
# 16      1234321       7       4
# 17
# 18
# 19
# 20

