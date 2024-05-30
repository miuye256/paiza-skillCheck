n, s = map(str, input().split())
n = int(n)

if s == "km":
    print(n * 1000000)
elif s == "m":
    print(n * 1000)
else:
    print(n * 10)