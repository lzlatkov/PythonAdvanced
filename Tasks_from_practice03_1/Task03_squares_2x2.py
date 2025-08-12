# Read user input
rows, columns = [int(num) for num in (input().split())]
matrix = [[el for el in input().split()] for row in range(rows)]
counter = 0
# Logic
for row_index in range(rows - 1):
    for column_index in range(columns - 1):
        if matrix[row_index][column_index] \
                == matrix[row_index][column_index + 1] \
                == matrix[row_index + 1][column_index] \
                == matrix[row_index + 1][column_index + 1]:
            counter += 1

# Print output
print(counter)