n = int(input())

matrix = []
player_position = []
collected_stars = 2
min_stars = 0
max_stars = 10
possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for row in range(n):
    row_data = input().split()
    matrix.append(row_data)
    if "P" in row_data:
        player_position = [row, row_data.index("P")]
        matrix[row][row_data.index("P")] = "."

while min_stars < collected_stars < max_stars:
    command = input()

    current_row = player_position[0]
    current_col = player_position[1]
    next_row_position = current_row + possible_moves[command][0]
    next_col_position = current_col + possible_moves[command][1]

    if next_row_position not in range(n) or next_col_position not in range(n):
        next_row_position = 0
        next_col_position = 0

    if matrix[next_row_position][next_col_position] == "*":
        collected_stars += 1
        matrix[next_row_position][next_col_position] = "."

    elif matrix[next_row_position][next_col_position] == "#":
        collected_stars -= 1
        continue

    player_position = [next_row_position, next_col_position]

if collected_stars == max_stars:
    print(f"You won! You have collected 10 stars.")
else:
    print(f"Game over! You are out of any stars.")
print(f"Your final position is {player_position}")
matrix[next_row_position][next_col_position] = "P"
for row in matrix:
    print(*row, sep=" ")