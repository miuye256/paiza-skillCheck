L, M, N = map(int, input().split())
ans = []

for i in range(L):
    ans.append("A")
for i in range(M):
    ans.append("B")
for i in range(N):
    ans.append("A")

print("".join(ans))