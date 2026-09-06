rows, columns = [int(i) for i in input().split()]
matrix = [['.' for _ in range(columns)] for _ in range(rows)]

for r in range(rows):  # 1
    for c in range(columns):
        if r % 2 == 0 and c % 2 != 0:
            matrix[r][c] = '*'
        elif r % 2 != 0 and c % 2 == 0:
            matrix[r][c] = '*'

for row in matrix:
    print(*row)

print()

matrix_2 = [['*' if (c + r) % 2 != 0 else '.' for c in range(columns)] for r in range(rows)]  # 2
for row in matrix_2:
    print(*row)