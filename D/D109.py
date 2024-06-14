date = "".join(input().split())

length = len(date)
count = date.count(date[0])
if length == count:
    print("Yes")
else:
    print("No")