X = int(input())
M = int(input())

if M % 30 == 0:
    print(M // 30 * X)
else:
    print(M // 30 * X + X)
