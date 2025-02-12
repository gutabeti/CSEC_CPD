s = input().strip()
uppercase_count = sum(1 for char in s if char.isupper())
lowercase_count = sum(1 for char in s if char.islower())
if uppercase_count > lowercase_count:
    corrected_word = s.upper()
else:
    corrected_word = s.lower()

print(corrected_word)
