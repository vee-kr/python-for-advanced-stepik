rows, columns = [int(x) for x in input().split()]
matrix = [[0 for _ in range(columns)] for _ in range(rows)]

numbers_fill = list(range(1, (rows * columns) + 1))

counter = 0
for r in range(rows):
    for c in range(columns):
        matrix[r][c] = numbers_fill[counter]
        counter += 1
        print(str(matrix[r][c]).ljust(3), end=' ')
    print()
