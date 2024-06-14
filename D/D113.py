h, m = map(int, input().split(":"))

if h < 8:
    h = h - 8 + 24
else:
    h -= 8
print(f"{h}:{m}")