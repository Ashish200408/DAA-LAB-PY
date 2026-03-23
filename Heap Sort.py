# Heap Sort Program

def heapify(arr, n, i):
    largest = i        # Assume root is largest
    left = 2 * i + 1   # Left child
    right = 2 * i + 2  # Right child

    # Check if left child is larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Step 1: Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[i], arr[0] = arr[0], arr[i]
        
        # Call heapify on reduced heap
        heapify(arr, i, 0)

    return arr


# Input
arr = list(map(int, input("Enter numbers separated by space: ").split()))

# Sorting
sorted_arr = heap_sort(arr)

# Output
print("Sorted array:", sorted_arr)