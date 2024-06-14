x = int(input())
num = 1
flag = False

while num < x:
    num *= 2
    if num == x:
        flag = True
        break
if flag:
    print("OK")
else:
    print("NG")