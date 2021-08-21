# 더하기 사이클_하중

c = int(input())
a = 0
a += c
count = 0
while True:
    if a < 10:
        if a + a < 10:
            a = a * 10 + a
        else:
            a = a * 10 + a % 10
    else:
        b = a % 10 + a // 10
        if b < 10:
            a = (a % 10) * 10 + b
        else:
            a = (a % 10) * 10 + b % 10
    count += 1
    if a == c:
        break

print(count)

# 조건을 걸 필요가 없었음..