string_1, string_2 = set(input().split()), set(input().split())

intersection = string_1.intersection(string_2)
print(len(intersection))