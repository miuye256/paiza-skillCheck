N = int(input())
result = []
count = 0

for i in range(N):
    a, b = input().split()

    if a == "n" or b == "n":
        result.append(i + 1)
        count += 1

print(count)
for i in range(count):
    print(result[i])