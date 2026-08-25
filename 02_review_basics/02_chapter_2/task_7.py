moves = ["камень", "ножницы", "бумага"]
answer = ["ничья", "Руслан", "Тимур"]
input_1, input_2 = input(), input()
if input_1 == input_2:  # 1
    flag = "ничья"

elif input_1 == "камень" and input_2 == "бумага":
    flag = "Руслан"

elif input_1 == "бумага" and input_2 == "ножницы":
    flag = "Руслан"

elif input_1 == "ножницы" and input_2 == "камень":
    flag = "Руслан"
else: flag = "Тимур"
print(flag)

difference = moves.index(input_1) - moves.index(input_2)  # 2
print(answer[difference])





