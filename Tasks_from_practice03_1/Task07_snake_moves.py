rows, columns = [int(num) for num in input().split()]
word = input()
matrix = [["" for _ in range(columns)] for row in range(rows)]
index = 0

for row in range(rows):
    if row % 2 == 0:
        for col in range(columns):
            matrix[row][col] = word[index]
            index = (index + 1) % len(word)
    else:
        for col in range(columns - 1, -1, -1):
            matrix[row][col] = word[index]
            index = (index + 1) % len(word)

for row in matrix:
    print("".join(row))