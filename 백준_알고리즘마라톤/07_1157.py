# 단어공부_하_문자열

text = input()
text = text.upper()
input_list = list(text)
input_list = set(input_list)

count_dict = {}
count_list = []
for i in input_list:
    count_dict[i] = text.count(i)
    count_list.append(text.count(i))
max_data = max(count_list)

count = 0
result = ''
for k, v in count_dict.items():
    if v == max_data:
        count += 1
        result += k
if count == 1:
    print(result)
else:
    print('?')