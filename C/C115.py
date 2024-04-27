N, M = map(int, input().split())
length_sum = 0

for i in range(N - 1):
    length = int(input())
    if length <= M:
        length_sum += length

print(length_sum)