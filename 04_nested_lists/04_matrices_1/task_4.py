rows_columns = int(input())
count = []
for _ in range(rows_columns):  # 1
    k = 0
    row = [int(num) for num in input().split()]
    mean = sum(row) / len(row)
    for elem in row:
        if elem > mean:
            k += 1
    count.append(k)
print(*count, sep="\n")


matrix = []   # 2
for _ in range(rows_columns):
    row = [int(num) for num in input().split()]
    matrix.append(row)

for r in range(rows_columns):
    k = 0
    mean = sum(matrix[r]) / rows_columns
    for c in range(rows_columns):
        if matrix[r][c] > mean:
            k += 1
    print(k)


