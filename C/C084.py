S = input()
length = len(S)
around = []

for i in range(length + 2):
    around.append("+")

around_str = ''.join(around)

print(around_str)
print('+' + S + '+')
print(around_str)