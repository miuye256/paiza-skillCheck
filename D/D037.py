M = int(input())
N = int(input())

if N % M != 0:
    print(N // M + 1)
else:
    print(N // M)