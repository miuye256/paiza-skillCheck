S = list(input())   # 入力をlistに変換
s = []  # 連続する-を除いた文字列を格納するリスト

# 連続する-を除いた文字列をsに格納
for str in S:
    s.append(str)   # 1文字ずつsに格納

    if len(s) > 1 and str == "-" and s[-2] == "-":
        s.pop(-1)

print("".join(s))


"""
S = input()
ans=""

ans=[c for i,c in enumerate(S) if i==0 or S[i-1]!=c or c!="-"]
print("".join(ans))
"""

"""
S = input()
for i in range(100):
    S=S.replace('--','-')
print(S)
"""
