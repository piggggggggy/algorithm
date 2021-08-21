# 알람 시계_하하

a,b = map(int,input().split())

time = a*60+b
min = (time-45)
if time >= 45 :
    print(min//60, min%60)
else:
    print(23,b+15)