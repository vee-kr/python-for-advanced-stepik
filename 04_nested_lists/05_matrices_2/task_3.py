rows, columns = int(input()), int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

i, j = [int(x) for x in input().split()]

for r in range(rows):
    matrix[r][i], matrix[r][j] = matrix[r][j], matrix[r][i]

for row in matrix:
    print(*row)
