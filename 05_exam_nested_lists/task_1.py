string, num =  input().split(), int(input())
answer = []
for i in range(num):
    row = []
    for j in range(i, len(string), num):
        row.append(string[j])
    answer.append(row)
print(answer)


