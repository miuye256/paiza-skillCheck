S = input()
check = [S[0] for i in range(len(S))]

if S == "".join(check):
    print("NG")
else:
    print("OK")