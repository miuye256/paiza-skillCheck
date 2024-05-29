n = input()

if len(n) == 3:
    print(n)
elif len(n) == 2:
    print("0" + n)
else:
    print("00" + n)


"""
n = list(input())

while len(n) < 3:
    n.insert(0, "0")
print("".join(n))
"""