r_1, r_2 = map(int, input().split())
R_1 = r_1
R_2 = r_2
for i in range(2):
    R_1 *= r_1
    R_2 *= r_2
print(R_1 - R_2)