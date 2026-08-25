Timur, Ruslan = input(), input()
answers_Timur = ["ножницыбумага", "бумагакамень", "каменьящерица", "ящерицаСпок",
                "Спокножницы", "ножницыящерица", "ящерицабумага", "Споккамень", "каменьножницы"]
if Timur == Ruslan:
    print("ничья")
elif (Timur + Ruslan) in answers_Timur:
    print("Тимур")
else:
    print("Руслан")