def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x<pivot]
    middle = [x for x in arr if x==pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
arr = [10,7,8,9,1,5]
print(quick_sort(arr))

# Time Complexity:
# Best Case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n^2) (when the smallest or largest element is always chosen as the pivot)

# space complexity: O(log n) on average, O(n) in the worst case (when the smallest or largest element is always chosen as the pivot)