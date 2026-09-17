num = int(input())

students = [tuple(input().split()) for _ in range(num)]
top_students = [elem for elem in students if elem[-1] in "45"]

for elem in students:
    print(*elem)

print()

for elem in top_students:
    print(*elem)

