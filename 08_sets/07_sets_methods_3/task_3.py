student_1, student_2, student_3 = set([int(x) for x in input().split()]),  set([int(x) for x in input().split()]),  set([int(x) for x in input().split()])
intersection_1_2 = student_1.intersection(student_2)
print(*sorted(intersection_1_2.difference(student_3), reverse=True))