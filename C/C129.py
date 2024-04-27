N, M = map(int, input().split())
A = []
B = []
judge = True

for i in range(M):
    A.append(int(input()))

for i in range(M):
    B.append(int(input()))

A.sort()
B.sort()

for i in range(M):
    if A[i] != B[i]:
        judge = False

if judge:
    print("Yes")
else:
    print("No")