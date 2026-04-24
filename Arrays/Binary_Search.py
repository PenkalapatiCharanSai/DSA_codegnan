# Search Operation in Array

def binary_Search(arr,target): # - O(log n) - Time complexity -> Because we are dividing the search space in half at each step
    low = 0
    high = (len(arr)) - 1

    
    while low <= high:
        mid = (low + high ) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = [10,20,30,40,50]
target = 20
print(binary_Search(arr, target))

# Time Complexity
# Best: O(1) - When the target is at the middle of the array
# Average: O(log n) - When the target is in the middle of the array
# Worst: O(log n) - When the target is not present in the array