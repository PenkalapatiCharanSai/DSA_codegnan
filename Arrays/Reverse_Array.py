# Reverse aN Array by k steps
 
def reversing_array(arr,k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]
arr = [1,2,3,4,5]
k = 2
print(reversing_array(arr, k))


def reverse(arr):
    result = []
    for i in range(len(arr)-1,-1,-1):
        result.append(arr[i])
    return result
arr = [1,2,3,4,5]
print(reverse(arr))