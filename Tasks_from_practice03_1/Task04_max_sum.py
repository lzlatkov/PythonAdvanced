rows, columns = [int(num) for num in input().split()]
matrix = [[int(el) for el in input().split()] for row in range(rows)]
max_sum = float("-inf")
max_row_position = 0
max_col_position = 0


for row_index in range(rows - 2):
    for col_index in range(columns - 2):
        current_sub_matrix_sum = 0
        for i in range(row_index, row_index + 3):
            for j in range(col_index, col_index + 3):
                current_sub_matrix_sum += matrix[i][j]
        if current_sub_matrix_sum > max_sum:
            max_sum = current_sub_matrix_sum
            max_row_position = row_index
            max_col_position = col_index

print(f"Sum = {max_sum}")
for row in range(max_row_position, max_row_position + 3):
    for col in range(max_col_position, max_col_position + 3):
        print(matrix[row][col], end=" ")
    print()