
#Finding Minimum value of an array
# arr = [2,10,16,5,4]
# min_val = arr[0]

# for i in range(1,len(arr)):
#     if arr[i] < min_val:
#         min_val = arr[i]
# print("Minimum: ", min_val)


#Finding Maximum value of an array
# arr = [2,10,16,5,4]
# max_val = arr[0]

# for i in range(1,len(arr)):
#     if arr[i] > max_val:
#         max_val = arr[i]
# print("Maximum: ", max_val)



arr = [2,10,16,5,4]
min_val = arr[0]
max_val = arr[0]
for i in range(1,len(arr)):
    if arr[i] < min_val:
        min_val = arr[i]
    if arr[i] > max_val:
        max_val = arr[i]
print("Minimum: ", min_val)
print("Maximum: ", max_val)