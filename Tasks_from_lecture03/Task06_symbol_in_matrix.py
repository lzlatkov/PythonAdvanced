# Read the size of the matrix
n = int(input())
matrix = []

# Logic
for row in range(n):
    row_data = [el for el in input()]
    matrix.append(row_data)

searched_symbol = input()
position = None
for row in range(n):
    for col in range(n):
        if matrix[row][col] == searched_symbol:
            position = (row, col)
            print(position)
            exit()

print(f"{searched_symbol} does not occur in the matrix")

