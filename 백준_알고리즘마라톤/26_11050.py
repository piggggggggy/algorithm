# 이항계수1_하_정수론 및 조합론
import sys

N, K = map(int, sys.stdin.readline().split())

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


print(int(factorial(N)/(factorial(K)*factorial(N-K))))


