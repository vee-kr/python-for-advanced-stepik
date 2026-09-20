from math import ceil, floor

def round_number(num):
    if num - int(num) < 0.5:
        return floor(num)
    return ceil(num)

num = int(input())
users_correct, answers_correct = set(), 0
for _ in range(num):
    user, ans = input().split(": ")
    if ans == "Correct":
        users_correct.add(user)
        answers_correct += 1

if answers_correct == 0:
    print("Вы можете стать первым, кто решит эту задачу")
else:
    percentage = round_number(answers_correct / num * 100)

    print(f"Верно решили {len(users_correct)} учащихся")
    print(f"Из всех попыток {percentage}% верных")



