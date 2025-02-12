n = int(input())
cards = list(map(int, input().split()))
sereja_score = 0
dima_score = 0
left = 0
right = n - 1
turn = 0  # 0 for Sereja, 1 for Dima

while left <= right:
    if cards[left] > cards[right]:
        if turn == 0:
            sereja_score += cards[left]
        else:
            dima_score += cards[left]
        left += 1
    else:
        if turn == 0:
            sereja_score += cards[right]
        else:
            dima_score += cards[right]
        right -= 1
    turn = 1 - turn  # Switch turns

print(sereja_score, dima_score)
