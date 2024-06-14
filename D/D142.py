N, X, Y = map(int, input().split())
count = [i for i in range(0, N, X)]

print(len(count) * Y)