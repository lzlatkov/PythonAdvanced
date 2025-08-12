rows, columns = [int(num) for num in input().split(", ")]
matrix = [[int(el) for el in input().split(", ")] for _ in range(rows)]
sub_matrix = []
max_sum = float("-inf")
current_sub_matrix_sum = 0

for row_index in range(rows - 1):
    for column_index in range(columns - 1):
        element = matrix[row_index][column_index]
        next_element = matrix[row_index][column_index + 1]
        below_element = matrix[row_index + 1][column_index]
        diagonal_element = matrix[row_index + 1][column_index + 1]
        current_sub_matrix_sum = element + next_element + below_element + diagonal_element
        if current_sub_matrix_sum > max_sum:
            max_sum = current_sub_matrix_sum
            sub_matrix = [[element, next_element], [below_element, diagonal_element]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)

