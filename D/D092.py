firstData = [int(x) for x in input().split()]
secondData = [int(x) for x in input().split()]


firstValue = firstData[2] / (firstData[0] * firstData[1])
secondValue = secondData[2] / (secondData[0] * secondData[1])

if firstValue < secondValue:
    print(" ".join(map(str, firstData)))
elif firstValue > secondValue:
    print(" ".join(map(str, secondData)))
else:
    print("DRAW")