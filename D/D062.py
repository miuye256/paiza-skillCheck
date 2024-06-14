h_1, h_2, h_3 = map(int, input().split())
figures = "ABCDEFGHIJ"

h_2 += h_1
h_3 += h_2
print(figures[0:h_1])
print(figures[h_1:h_2])
print(figures[h_2:h_3])