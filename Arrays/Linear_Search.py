#Search Operation in Array

# 1. Linear Search

def linear_Search(arr,target):  # Indexed based approach
    for i in range(len(arr)):    
        if arr[i] == target:
            return i
    return -1
arr = [10,20,40,50,30]
target = 30
print(linear_Search(arr,target))


def linear_Search(arr,target):   # - Direct approach
    for i in arr:               
        if i == target:
            return i
    return -1
#arr = [10,20,30,40,50]
arr = list(map(int,input().split()))
target = 30
print(linear_Search(arr,target))


#Time Complexity
#Best: O(1) - When the target is at the first position of the array
#Average: O(n) - When the target is in the middle of the array
#Worst: O(n) - When the target is not present in the array