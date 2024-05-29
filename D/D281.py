X = int(input())
Y_1, Y_2, Y_3 = map(int, input().split())

if X >= Y_1 + Y_2 + Y_3:
    print("OK")
else:
    print("NG")