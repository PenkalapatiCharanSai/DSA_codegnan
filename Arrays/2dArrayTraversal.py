# 2D Array Traversal
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# Row-wise
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end=" ")

# Column-wise
for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        print(matrix[i][j],end=" ")

# Using for-each loop
for row in matrix:
    for val in row:
        print(val,end=" ")