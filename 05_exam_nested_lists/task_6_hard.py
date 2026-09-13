num = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(num)]
flag = "YES"
matrix_new = []

target_numbers = list(range(1, num + 1))

for r in range(num):
    row = []
    for c in range(num):
        row.append(matrix[c][r])
    matrix_new.append(row)

for r in range(num):

    for elem in target_numbers:
        if elem not in matrix_new[r] or  elem not in matrix[r]:
            flag = "NO"
            break


print(flag)

