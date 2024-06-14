S = input()
countHyphen = S.count("-")
countUnderbar = S.count("_")

if countHyphen <= countUnderbar:
    ans = S.replace("-", "_")
else:
    ans = S.replace("_", "-")
print(ans)