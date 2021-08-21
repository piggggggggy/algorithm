# 셀프넘버_하_함수

# 10,000보다 작거나 같은 수
# 33 + 3 + 3 = 39
# 39 + 3 + 9 = 51
# 51 + 5 + 1 = 57
# .
# .
# .
# 111 + 1 + 1 + 1 = 114

def d(n):
    m = str(n)
    for i in m:
        n += int(i)
    return n

not_self_nums = []
nums = range(1,10000)
for i in nums:
    not_self_num = d(i)
    if not_self_num <10000:
        not_self_nums.append(not_self_num)

not_self_nums = set(not_self_nums)
nums = set(nums)
self_nums = sorted(nums - not_self_nums)
for l in self_nums:
    print(l)




# a = set(range(1, 10001))
# b = set()
# for x in range(1, 10001):
#     for y in str(x):
#         x += int(y)
#     b.add(x)
#
# selfNums = sorted(a - b)
# for selfNum in selfNums:
#     print(selfNum)