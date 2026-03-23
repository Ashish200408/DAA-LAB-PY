# Huffman Coding Tree Construction

import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # For priority queue comparison
    def __lt__(self, other):
        return self.freq < other.freq


# Function to build Huffman Tree
def build_huffman_tree(char_freq):
    heap = []

    # Create leaf nodes and push into heap
    for char, freq in char_freq.items():
        heapq.heappush(heap, Node(char, freq))

    # Build tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]  # Root node


# Generate Huffman Codes
def generate_codes(root, current_code="", codes={}):
    if root is None:
        return

    # If leaf node
    if root.char is not None:
        codes[root.char] = current_code

    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)

    return codes


# -----------------------------
# Input
# -----------------------------
text = input("Enter text: ")

# Calculate frequency of characters
char_freq = {}
for char in text:
    char_freq[char] = char_freq.get(char, 0) + 1

# Build tree
root = build_huffman_tree(char_freq)

# Generate codes
huffman_codes = generate_codes(root)

# Output
print("\nHuffman Codes:")
for char, code in huffman_codes.items():
    print(f"{char}: {code}")