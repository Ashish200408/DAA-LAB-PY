# Selection Sort Program

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Assume current position has minimum
        min_index = i

        # Find the minimum element in remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum with first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Taking input from user
arr = list(map(int, input("Enter numbers separated by space: ").split()))

# Sorting
sorted_arr = selection_sort(arr)

# Output
print("Sorted array:", sorted_arr)