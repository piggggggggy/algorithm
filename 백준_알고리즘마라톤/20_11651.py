# 좌표 정렬하기 2_중_정렬

N = int(input())

lst = []
for i in range(N):
    xy = list(map(int, input().split()))
    lst.append(xy)

# lst.sort(key=lambda x: (x[1], x[0]))

result = sorted(lst, key=lambda x: (x[1], x[0]))

for j in result:
    print(str(j[0])+" "+str(j[1]))


# 굉장히 오래걸림
# import sys???
# import stdin???
# 이거 이용해서 풀면 빨라지는듯.. 뭔지모름