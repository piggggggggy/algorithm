# 베르트랑 공준_하_기본수학2
#
# import sys
#
# n = 123456 * 2 + 1
#
# prime_nums = [True] * n
# m = int(n ** 0.5)
# for i in range(2, m+1):
#     if prime_nums[i]:
#         for j in range(i+i, n, i):
#             prime_nums[j] = False
#
#
#
# while True:
#     check_num = int(sys.stdin.readline())
#     if check_num == 0:
#         break
#     print(len([i for i in range(check_num+1, check_num * 2 + 1) if prime_nums[i] == True]))


# 소수를 다루는 법과 (에라토스테네스의 체) 식을 간소화, 시간복잡도를 줄이는 법을 생각하자!


from sys import stdin
import math



while True:
    number = int(stdin.readline())
    if 1 <= number <= 123456:
        count = 0
        for num in range(number + 1, number * 2 + 1):
            count_divisor = 0
            range_num = int(math.sqrt(num))

            for i in range(1, range_num + 1):
                if num % i == 0:
                    count_divisor += 1

            if count_divisor == 1:
                count += 1

        print(count)
    else:
        break