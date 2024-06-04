N = int(input())
hand = [i for i in input().split()]
G = 0
P = 0

for i in hand:
    if i == "G":
        G += 1
    else:
        P += 1
if G == P:
    print("Draw")
elif G < P:
    print("G")
else:
    print("P")