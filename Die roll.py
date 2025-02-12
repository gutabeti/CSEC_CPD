import math
Y, W = map(int, input().split())
max_roll = max(Y, W)
favorable = 6 - max_roll + 1
gcd = math.gcd(favorable, 6)
numerator = favorable // gcd
denominator = 6 // gcd
print(f"{numerator}/{denominator}")
