rows_columns = int(input())
matrix = []
for _ in range(rows_columns):
    row = [int(num) for num in input().split()]
    matrix.append(row)

total = 0
for r in range(rows_columns):
    total += matrix[r][r]

print(total)