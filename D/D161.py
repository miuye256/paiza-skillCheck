N = int(input())
count = 0

for i in range(7):
    count += int(input())
if N >= count:
    print(count)
else:
    print(N)