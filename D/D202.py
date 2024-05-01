p_1, f_1 = map(int, input().split())
p_2, f_2 = map(int, input().split())
if p_1 + f_1 < p_2 + f_2:
    print(p_1 + f_1)
elif p_1 + f_1 > p_2 + f_2:
    print(p_2 + f_2)
else:
    print(p_1 + f_1)