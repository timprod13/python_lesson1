# нахождение наибольшего числа

n = input("Введите число ")
result = 0
for i in n:
    while int(i) > result:
        result = int(i)
print("Наибольшая цифра в числе - ", result)
