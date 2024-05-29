X, P = map(int, input().split())

c = X - P
if c < 0:
    print(0)
else:
    print(c)