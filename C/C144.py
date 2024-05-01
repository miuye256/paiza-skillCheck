N = int(input())
A = [0] * N
B = [0] * N
count = 0
for i in range(N):
    A[i], B[i] = map(str, input().split())
    if A[i] == "G" and B[i] == "C" or A[i] == "C" and B[i] == "P" or A[i] == "P" and B[i] == "G":
        count += 1
print(count)