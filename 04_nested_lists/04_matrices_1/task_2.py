rows, columns = int(input()), int(input())
matrix = [[input() for _ in range(columns)] for _ in range(rows)]

for row in matrix:
    print(*row)

print()

for c in range(columns):
    for r in range(rows):
        print(matrix[r][c], end=" ")
    print()