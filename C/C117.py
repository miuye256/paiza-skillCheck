N, M = map(int, input().split())
A, B, C = map(int, input().split())

R = []

count = 0

for i in range(N):
    R.append(int(input()))
    profit = C * R[i] - A - B * M
    
    if profit < 0:
        count += 1

print(count)