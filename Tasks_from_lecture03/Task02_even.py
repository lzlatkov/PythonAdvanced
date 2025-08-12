rows = int(input())
matrix = []
even_matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split(", ") if int(el) % 2 == 0])

print(matrix)
# for el in range(len(matrix)):
#     even_matrix.append([])
#     for cow_index in range(len(matrix[el])):
#         if matrix[el][cow_index] % 2 == 0:
#             even_matrix[el].append(matrix[el][cow_index])
#
# print(even_matrix)




#matrix.append([int(el) for el in input().split(", ")] for _ in range(int(input())))