num_rows_columns = int(input())
matrix_1 = [[int(i) for i in input().split()] for _ in range(num_rows_columns)]
power = int(input())

matrix_repeat = [[matrix_1[r][c] for c in range(num_rows_columns)] for r in range(num_rows_columns)]

for _ in range(power-1):

    matrix_3 = []
    for r in range(num_rows_columns):
        row = []

        for col in range(num_rows_columns):
            total = 0
            for c in range(num_rows_columns):

                total += matrix_1[r][c] * matrix_repeat[c][col]

            row.append(total)
        matrix_3.append(row)
    matrix_1 = matrix_3

for row in matrix_3:
    print(*row)










