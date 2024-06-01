N = int(input())
M, A, B = map(int, input().split())

if N >= M:
    print(N * A)
else:
    print(N * B)