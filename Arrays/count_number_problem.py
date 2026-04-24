# Count how many times the number appears 
# arr = [1, 2, 2, 3, 1]
# k = 2
# o/p = 3

def count_occurrences(arr,k):
    count = 0
    for num in arr:
        if num == k:
            count += 1
    return count
arr = [1,2,2,3,2]
k = 2
print(count_occurrences(arr, k))