S = input()
ans = ""

for i in S:
    if i == "0":
        ans +="C"
    elif i == "1":
        ans += "A"
    else:
        ans += "B"
print(ans)