# Insertion Sort
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while  j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
arr = [5,3,2,4]
print(insertion_sort(arr)) 

# Time Complexity:
# Best Case: O(n) (when the array is already sorted)
# Average Case: O(n^2) (when the array is in random order)
# Worst Case: O(n^2) (when the array is sorted in reverse order)

# Space Complexity: O(1) (in-place sorting algorithm)