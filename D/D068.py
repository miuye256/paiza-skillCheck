n = int(input())
s = input()

ans = "{} {}".format(s.count(str(n)), s.find(str(n)))
print(ans)