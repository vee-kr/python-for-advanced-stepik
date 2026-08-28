num = int(input())
result = []
for i in range(1, num + 1):
    result.append(list(range(1, i + 1)))
print(*result, sep='\n')
