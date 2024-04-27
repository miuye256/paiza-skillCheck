N, D = map(int, input().split())
over = []
sum = 0

for i in range(N - 1):
    over.append(int(input()))

for i in range(N - 1):
    sum += over[i]

print(D * (D * N - sum))