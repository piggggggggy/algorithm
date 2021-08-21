# 잃어버린 괄호_중

import sys

text = sys.stdin.readline()

plus_list = list(text.strip().split('-'))
first = int(sum(map(int, plus_list[0].strip().split('+'))))

for i in plus_list[1:]:
    first -= sum(map(int, i.strip().split('+')))

print(first)
