# Read user input
matrix = [[int(num) for num in input().split()] for row in range(int(input()))]

primary_diagonal_elements = []
secondary_diagonal_elements = []

# Logic
for row, column in zip(range(0, len(matrix)), range(len(matrix) - 1, -1, -1)):
    primary_diagonal_elements.append(matrix[row][row])
    secondary_diagonal_elements.append(matrix[row][column])

# Print output
print(abs(sum(primary_diagonal_elements) - (sum(secondary_diagonal_elements))))

