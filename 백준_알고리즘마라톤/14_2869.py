# 달팽이는 올라가고 싶다_중하_기본수학1

A, B, V = map(int, input().split())

move = A-B
pre_count = V-A
if pre_count > 0 :
    if pre_count % move > 0 :
        print(pre_count//move+2)
    else:
        print(pre_count//move+1)
else:
    print(1)
