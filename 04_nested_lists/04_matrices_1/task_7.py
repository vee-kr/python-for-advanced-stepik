num_rows_columns = int(input())
matrix = []
for _ in range(num_rows_columns):
    row = [int(i) for i in input().split()]
    matrix.append(row)

quadrant_up, quadrant_down, quadrant_left, quadrant_right = [], [], [], []
for r in range(num_rows_columns):
    for c in range(num_rows_columns):
        if c > r and r < num_rows_columns - 1 - c:  # up quarter
            quadrant_up.append(matrix[r][c])
        elif c > r and r > num_rows_columns - 1 - c:  # right quarter
            quadrant_right.append(matrix[r][c])
        elif c < r and r < num_rows_columns - 1 - c:  # left quarter
            quadrant_left.append(matrix[r][c])
        elif c < r and r > num_rows_columns - 1 - c:  # down quarter
            quadrant_down.append(matrix[r][c])


print(f"Верхняя четверть: {sum(quadrant_up)}",
      f"Правая четверть: {sum(quadrant_right)}",
      f"Нижняя четверть: {sum(quadrant_down)}",
      f"Левая четверть: {sum(quadrant_left)}", sep='\n')
