N = int(input())
a = int(input())

if N % a != 0:
    print(N // a + 1)
else:
    print(N // a)