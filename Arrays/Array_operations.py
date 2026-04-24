arr = [10,20,30,40]    
# 1. Insert Operation

# Insert at End
arr.append(50)       #O(1) - Time complexity -> Because we are inserting at the end of the array
print(arr)

# Insert at Beginning
arr.insert(0,1)         # O(n) - Time complexity -> Because we have to shift all the elements to the right
print(arr)

# Insert at any position
arr.insert(2,15)           #O(n) - Time complexity -> Because we have to shift all the elements to the right
print(arr)



# 2. Delete Operation

# 1. Delete by value
arr.remove(30)           # O(n) - Time complexity -> Because we have to search for the element first
print(arr)

# 2. Delete by index
arr.pop(1)          # O(n) - Time complexity -> Because we have to shift all the elements to the left
print(arr)

# 3. Update(Replace) in Arrays
# - Replace value ar a given index
# - No shifting required
# Original: [10,20,30,40]
# Result: [10,20,99,40]

arr[2] = 99   # O(1) - Time complexity -> Because we are replacing the value at a given index
print(arr)
