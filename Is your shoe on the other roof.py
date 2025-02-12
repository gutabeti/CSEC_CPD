s1, s2, s3, s4 = map(int, input().split())
unique_colors = {s1, s2, s3, s4}
additional_horseshoes = 4 - len(unique_colors)
print(additional_horseshoes)
