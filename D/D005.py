m, n = map(int, input().split())
ans = []

for i in range(10):
    ans.append(str(m))
    m += n
print(" ".join(ans))

"""
m, n = map(int, input().split())
ans = [str(m + i * n) for i in range(10)]
print(" ".join(ans))
"""