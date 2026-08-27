largest = []
for el in list1:  # 1
    largest.append(max(el))

print(max(largest))

largest = [max(el) for el in list1]  # 2
print(max(largest))
