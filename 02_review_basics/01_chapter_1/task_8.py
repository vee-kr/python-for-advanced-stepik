n, step = int(input()), int(input())
numbers = list(range(1, n + 1))

while len(numbers) != 1:  # 1
    for _ in range(step-1):
        numbers.append(numbers.pop(0))
    del numbers[0]

print(*numbers)


index = 1  # 2
while len(numbers) > 1:
    index = (index + step - 1) % len(numbers)
    del numbers[index]
print(numbers[0] - 1)



