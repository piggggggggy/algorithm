# 그룹단어체커_하_문자열

num = int(input())
count = 0
for n in range(num):
    text = input()
    alph_list = [text[0]]
    for i in range(len(text)-1):
        if text[i] != text[i+1]:
            if text[i+1] not in alph_list:
                alph_list.append(text[i+1])
            else:

                count += 1
                break

print(num - count)