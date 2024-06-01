T = int(input())

if T % 24 == 0:
    print(T // 24)
else:
    print(T // 24 + 1)