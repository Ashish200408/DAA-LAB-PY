# Fake Coin Problem using Divide and Conquer

def find_fake_coin(coins, left, right):
    # Base case: only one coin
    if left == right:
        return left

    mid = (left + right) // 2

    # Calculate weights of both halves
    left_sum = sum(coins[left:mid+1])
    right_sum = sum(coins[mid+1:right+1])

    # Compare weights
    if left_sum < right_sum:
        # Fake coin is in left half
        return find_fake_coin(coins, left, mid)
    else:
        # Fake coin is in right half
        return find_fake_coin(coins, mid+1, right)


# -----------------------------
# Example Input
# -----------------------------

# 1 represents normal coin, smaller value (e.g., 0.5) represents fake coin
coins = list(map(float, input("Enter coin weights: ").split()))

# Find fake coin index
fake_index = find_fake_coin(coins, 0, len(coins) - 1)

print(f"Fake coin found at position: {fake_index}")