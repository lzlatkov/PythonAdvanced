num = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(num)]
diagonal_sym = 0

for row in range(num):
    for col in range(num):
        if row == col:
            diagonal_sym += matrix[row][col]

print(diagonal_sym)