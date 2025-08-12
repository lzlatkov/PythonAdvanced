user_input = input().split("|")

matrix = []

for index in range(len(user_input) - 1, -1, -1):
    row = user_input[index].split()
    if row:
        matrix.append(row)

for row in matrix:
    print(*row, end=" ")

