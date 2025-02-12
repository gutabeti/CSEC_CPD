s = input().strip()
t = input().strip()
position = 1
for instruction in t:
    if position <= len(s) and s[position - 1] == instruction:
        position += 1

print(position)
