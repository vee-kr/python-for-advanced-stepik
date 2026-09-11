rows, columns = [int(x) for x in input().split()]
matrix = [[0 for _ in range(columns)] for _ in range(rows)]

counter = 1

left, top, right, bottom = 0, 0, columns, rows

while counter <= rows * columns:

    for i in range(left, right):
        matrix[top][i] = counter
        counter += 1
    top += 1

    if top < bottom:
        for i in range(top, bottom):
            matrix[i][right-1] = counter
            counter += 1

    right -= 1

    if left < right and top < bottom:
        for i in range(right-1, left - 1, -1):
            matrix[bottom-1][i] = counter
            counter += 1

    bottom -= 1

    if top < bottom and left < right:
        for i in range(bottom-1, top - 1, -1):
            matrix[i][left] = counter
            counter += 1

    left += 1


for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end=" ")
    print()

