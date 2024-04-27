N = int(input())

time = []

for i in range(N):
    s, f, t = map(int, input().split())
    time.append(s+ f + (24 - t))

print(min(time))
print(max(time))