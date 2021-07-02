a = ['99', '989', '99111112', '6', '888', '1000']


a = sorted(map(str, a), key=lambda x: x*3, reverse=True)


print(a)



