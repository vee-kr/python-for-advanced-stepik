numbers = [int(i) for i in input().split()]

numbers.insert(0, numbers.pop(-1))
print(*numbers)