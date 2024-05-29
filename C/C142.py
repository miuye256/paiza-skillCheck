S = input()
N = int(input())
T = [i for i in input().split()]

for i in range(N):
    if S == T[i]:
        print("Yes")
        exit()
print("No")