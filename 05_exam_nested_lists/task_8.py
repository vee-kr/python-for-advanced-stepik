num = int(input())
matrix = [[0 for _ in range(num)] for _ in range(num)]
for r in range(num):
    for c in range(num):
        matrix[r][c] = abs(r - c)
for row in matrix:
    print(*row)