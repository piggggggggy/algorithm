# 나무 자르기_중_이분탐색

N, M = map(int, input().split())

height_list = list(map(int, input().split()))

high_value = max(height_list)
low_value = 0
target_height = 0
while low_value <= high_value:
    mid = int((high_value + low_value) // 2)
    cut_list = sum([i - mid if i > mid else 0 for i in height_list])
    if cut_list < M:
        high_value = mid - 1
    elif cut_list >= M:
        low_value = mid + 1
        if target_height < mid:
            target_height = mid

print(target_height)





# 꼭 다시풀어보고 이분탐색을 문제에 적용하는 법을 깨우치자