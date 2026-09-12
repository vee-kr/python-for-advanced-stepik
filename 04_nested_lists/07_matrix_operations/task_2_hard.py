rows_1, columns_1 = [int(x) for x in input().split()]
matrix_1 = [[int(x) for x in input().split()] for _ in range(rows_1)]
input()

rows_2, columns_2 = [int(x) for x in input().split()]
matrix_2 = [[int(x) for x in input().split()] for _ in range(rows_2)]

matrix_3 = []


for r in range(rows_1):
    row = []

    for col in range(columns_2):
        total = 0
        for c in range(columns_1):

            total += matrix_1[r][c] * matrix_2[c][col]

        row.append(total)
    matrix_3.append(row)


for row in matrix_3:
    print(*row)






