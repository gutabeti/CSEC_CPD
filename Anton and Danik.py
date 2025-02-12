n = int(input())
s = input().strip()
count_A = s.count('A')
count_D = s.count('D')

if count_A > count_D:
    print("Anton")
elif count_D > count_A:
    print("Danik")
else:
    print("Friendship")
