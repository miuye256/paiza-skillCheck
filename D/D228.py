S, T = map(int, input().split())
H, M = map(int, input().split())

if S > H:
    print("Yes")
elif S == H and T >= M:
    print("Yes")
else:
    print("No")