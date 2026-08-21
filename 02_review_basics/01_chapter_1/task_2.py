def body_mass_index(w, h):
    bmi = w / h ** 2
    if bmi > 25:
        return "Избыточная масса"
    elif bmi < 18.5:
        return "Недостаточная масса"
    else:
        return "Оптимальная масса"


weight, height = float(input()), float(input())
print(body_mass_index(weight, height))