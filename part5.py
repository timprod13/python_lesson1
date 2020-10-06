# нахождение прибыли фирмы в расчете на одного сотрудника

proceeds = int(input("Введите выручку фирмы "))
costs = int(input("Введите издержки фирмы "))
if proceeds > costs:
    print("Ваша фирма работает в прибыль!")
    print(f"Рентабельность выручки равна {proceeds / costs:.2f}")
    employees = int(input("Введите количество сотрудников "))
    print(f"Прибыль фирмы в расчете на одного сотрудника равна {proceeds / costs:.2f}")
elif proceeds < costs:
    print("Ваша фирма работает несет убытки!")
else:
    print("Ваша фирма вышла в ноль!")
