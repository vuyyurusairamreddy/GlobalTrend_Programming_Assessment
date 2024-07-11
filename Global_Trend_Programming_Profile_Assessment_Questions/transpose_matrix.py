# Filename: transpose_matrix.py

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix before :" +str(matrix))
print("Transpose of matrix is: " + str(transpose(matrix)))  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
