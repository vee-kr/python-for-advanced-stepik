rows_columns = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows_columns)]

new_matrix = []   # 1
for c in range(rows_columns):
    row = []
    for r in range(rows_columns):
        row.append(matrix[r][c])

    new_matrix.append(row)

if matrix == new_matrix:
    print("YES")
else: print("NO")


is_symmetric = "YES"  # 2
for r in range(rows_columns):
    for c in range(r + 1, rows_columns):
        if matrix[r][c] != matrix[c][r]:
            is_symmetric = "NO"
            break

print(is_symmetric)




