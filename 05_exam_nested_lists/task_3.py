num = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(num)]

matrix_new = []

for r in range(num):
    row = []
    for c in range(num):
        row.append(matrix[c][r])
    matrix_new.append(row)

for row in matrix_new:
    print(*row)
