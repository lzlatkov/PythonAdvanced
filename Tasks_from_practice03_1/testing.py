matrix = []
matrix_size = int(input())

for row in range(matrix_size):
    row_index = input().split(", ")
    matrix.append(row_index)
    for col in range(matrix_size):
        first_el = matrix[row][col]

        print(first_el)