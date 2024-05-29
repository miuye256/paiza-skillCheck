a = [int(i) for i in input().split()]
count = 0

for i in range(7):
    count += a[i]

if count >= 5:
    print("yes")
else:
    print("no")