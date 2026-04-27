# Selection Sort
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr = [5,3,2,4]
print(selection_sort(arr))

# Time Complexity:
# Best Case: O(n^2) (regardless of the initial order of the array)
# Average Case: O(n^2) (when the array is in random order)
# Worst Case: O(n^2) (when the array is sorted in reverse order)


# Space Complexity: O(1) (in-place sorting algorithm)