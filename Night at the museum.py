s = input().strip()
current = 'a'
total_rotations = 0
for char in s:
    # Calculate the absolute difference in ASCII values
    diff = abs(ord(char) - ord(current))
    # The minimum rotations is the minimum of the clockwise and counterclockwise distances
    rotations = min(diff, 26 - diff)
    total_rotations += rotations
    current = char

print(total_rotations)
