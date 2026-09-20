numbers = [int(elem) for elem in input().split()]
no_repeat_numbers = set()
for number in numbers:
    if number not in no_repeat_numbers:
        no_repeat_numbers.add(number)
        print("NO")
    else:
        print("YES")
