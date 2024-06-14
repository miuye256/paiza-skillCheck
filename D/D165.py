s = input()

for i in s:
    if s.count(i) > 1:
        print("NG")
        exit()
print("OK")