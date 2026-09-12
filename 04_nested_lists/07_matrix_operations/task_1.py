rows, columns = [int(x) for x in input().split()]
matrix_1 = [[int(i) for i in input().split()] for _ in range(rows)]
print(input())
matrix_2 = [[int(i) for i in input().split()] for _ in range(rows)]

matrix_3 = [[0 for _ in range(columns)] for _ in range(rows)]

for r in range(rows):
    for c in range(columns):
        matrix_3[r][c] = matrix_1[r][c] + matrix_2[r][c]

for row in matrix_3:
    print(*row)