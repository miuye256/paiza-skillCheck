m, p, q = map(int, input().split())

m -= m * (p / 100)
m -= m * (q / 100)

print(m)