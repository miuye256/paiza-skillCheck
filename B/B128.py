def replace(count, number, output):
    content = ["." for i in range(9)]
    number = int(number)

    for i in range(number):
        content[i] = "#"

    if count % 3 == 0:
        for i in range(9):
            output[int(i / 3)][i % 3] = content[i]
    if count % 3 == 1:
        for i in range(9):
            output[int(i / 3)][i % 3 + 3] = content[i]
    if count % 3 == 2:
        for i in range(9):
            output[int(i / 3)][i % 3 + 6] = content[i]

N = input()
digits = int(len(N) / 3)
output = [["." for j in range(9)] for i in range(3)]
count = 0

for i in range(digits):
    for i in range(3):
        replace(count, N[count], output)
        count += 1
    print(*output[0], sep = "")
    print(*output[1], sep = "")
    print(*output[2], sep = "")