rows, columns = [int(x) for x in input().split()]
matrix = [[0 for _ in range(columns)] for _ in range(rows)]

for c in range(columns):
    for r in range(rows):
        matrix[r][c] = c * rows + r + 1

for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end=' ')
    print()