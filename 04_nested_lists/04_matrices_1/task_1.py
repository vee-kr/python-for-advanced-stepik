n, m = int(input()), int(input())
matrix = []

for _ in range(n):
    temp = []

    for _ in range(m):
        temp.append(input())


    matrix.append(temp)

for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()