t = [int(input()) for i in range(7)]
ans = 0

for i in t:
    if i <= 30:
        ans += 1
print(ans)