# Find the first occurance number
# Input: [1,2,3,2,3,2]
# Output: 1

def first_occurance(arr,x):
    low = 0
    high = (len(arr)) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            ans = mid
            high = mid - 1 # go left
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return ans
arr = [1,2,2,2,3]
x = 2
print(first_occurance(arr, x)) 