N, L = map(int, input().split())
x = [int(input()) for i in range(N)]

for i in range(N):
    if L > x[i]:
        L += x[i] // 2
    elif L < x[i]:
        L //= 2

print(L)