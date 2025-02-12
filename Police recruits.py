n = int(input())
events = list(map(int, input().split()))
available_recruits = 0
untreated_crimes = 0

for event in events:
    if event == -1:
        if available_recruits > 0:
            available_recruits -= 1
        else:
            untreated_crimes += 1
    else:
        available_recruits += event

print(untreated_crimes)
