N, M = map(int, input().split())

if N % 2 == 0 and M % 2 == 1:
    print("YES")
elif N % 2 == 1 and M % 2 == 0:
    print("YES")
else:
    print("NO")