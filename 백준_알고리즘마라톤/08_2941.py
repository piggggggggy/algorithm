# 크로아티아 알파벳_하_문자열

text = input()

cro_alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


for i in cro_alph:
    text = text.replace(i,"1")
result = len(text)

print(result)