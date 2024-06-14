n = input()
count = n.count(n[0])

if count == len(n):
    print(n)
else:
    print("No")