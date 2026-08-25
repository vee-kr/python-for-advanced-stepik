num = int(input())
count_1, count_2, count_3, count_4 = 0, 0, 0, 0
for _ in range(num):
    coordinates = [int(i) for i in input().split()]
    x, y = coordinates[0], coordinates[1]
    if x > 0 and y > 0:
        count_1 += 1
    elif x > 0 and y < 0:
        count_4 += 1
    elif x < 0 and y > 0:
        count_2 += 1
    elif x < 0 and y < 0:
        count_3 += 1


print(f"Первая четверть: {count_1}")
print(f"Вторая четверть: {count_2}")
print(f"Третья четверть: {count_3}")
print(f"Четвертая четверть: {count_4}")