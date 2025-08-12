row_count, column_count = [int(num) for num in input().split(", ")]
matrix = []

# for row in range(row_count):
#     row_data = [int(el) for el in input().split()]
#     matrix.append(row_data)

matrix = [[int(el) for el in input().split()] for row in range(row_count)]

for col in range(column_count):
    col_sum = 0
    for row in range(row_count):
        col_sum += matrix[row][col]
    print(col_sum)

