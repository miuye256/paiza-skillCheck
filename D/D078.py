a = [int(i) for i in input().split()]
X = int(input())

if sum(a) / len(a) >= X:
    print("pass")
else:
    print("failure")