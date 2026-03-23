# Horspool's String Matching Algorithm

def build_shift_table(pattern):
    m = len(pattern)
    shift_table = {}

    # Initialize all characters with default shift = m
    for char in set(pattern):
        shift_table[char] = m

    # Fill shift values based on pattern
    for i in range(m - 1):
        shift_table[pattern[i]] = m - 1 - i

    return shift_table


def horspool(text, pattern):
    n = len(text)
    m = len(pattern)

    shift_table = build_shift_table(pattern)

    i = m - 1  # Index in text

    while i < n:
        k = 0

        # Match pattern from right to left
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1

        if k == m:
            return i - m + 1  # Match found

        # Shift based on table
        shift = shift_table.get(text[i], m)
        i += shift

    return -1  # No match


# Input
text = input("Enter text: ")
pattern = input("Enter pattern: ")

# Search
result = horspool(text, pattern)

# Output
if result != -1:
    print(f"Pattern found at index {result}")
else:
    print("Pattern not found")