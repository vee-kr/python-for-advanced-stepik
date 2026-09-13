num = int(input())
matrix = [['.' for _ in range(num)] for _ in range(num)]

for r in range(num):
    for c in range(num):
        matrix[r][r] = '*'
        matrix[r][num - 1 - r] = '*'
        if num // 2 == c:
            matrix[r][c] = "*"
        if num // 2 == r:
            matrix[r][c] = "*"
for row in matrix:
    print(*row)
