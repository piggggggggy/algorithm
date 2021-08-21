# 평균은 넘겠지_하_1차원 배열

n = int(input())
for i in range(n):
    scores = list(map(int, input().split()))
    nn = scores.pop(0)
    avg = sum(scores)/nn
    avg_up = [j for j in scores if j > avg]
    result = len(avg_up)/nn
    print('%.3f' % round(result*100, 3)+'%')