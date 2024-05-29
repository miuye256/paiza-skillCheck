P_1, P_2 = map(int, input().split())
N = int(input())
P_1 -= N
P_2 -= N
print(" ".join([str(P_1), str(P_2)]))