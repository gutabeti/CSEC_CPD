k, r = map(int, input().split())
n = 1
while True:
    total_cost = n * k
    if total_cost % 10 == r or total_cost % 10 == 0:
        break
    n += 1

print(n)
