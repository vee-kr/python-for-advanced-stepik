numbers = [int(i) for i in input().split()]
counter = 0
for i in range(len(numbers) - 1):
    if numbers[i + 1] > numbers[i]:
        counter += 1
print(counter)
