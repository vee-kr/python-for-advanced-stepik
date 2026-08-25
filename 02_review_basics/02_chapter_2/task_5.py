numbers = [int(i) for i in input().split()]
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print(len(unique_numbers))