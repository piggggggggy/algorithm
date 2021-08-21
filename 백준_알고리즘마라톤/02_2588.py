# # 곱셈_하하
A = int(input())
B = input()

var1 = A*int(B[2])
var2 = A*int(B[1])
var3 = A*int(B[0])


print(var1)
print(var2)
print(var3)
print(var1+var2*10+var3*100)



# import sys
#
# A = int(sys.stdin.readline())
# B = sys.stdin.readline()
#
# var1 = A*int(B[2])
# var2 = A*int(B[1])
# var3 = A*int(B[0])
#
#
# print(var1)
# print(var2)
# print(var3)
# print(var1+var2*10+var3*100)



a,b=int(input()),input()

print(*(a*int(p) for p in b[::-1]),a*int(b),sep="\n")









