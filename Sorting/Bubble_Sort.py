# Bubble Sort
def bubble_sort(arr):
    n= len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
arr = [5,3,2,4]
print(bubble_sort(arr))

# Time Complexity: 
# Best Case: O(n) (when the array is already sorted)
# Average Case: O(n^2) (when the array is in random order)
# Worst Case: O(n^2) (when the array is sorted in reverse order)

# Space Complexity: O(1) (in-place sorting algorithm)