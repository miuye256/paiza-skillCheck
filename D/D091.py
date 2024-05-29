p = [int(i) for i in input().split()]
ans = 0

for i in range(10):
    if p[i] <= 2:
        ans += 1

print(ans)