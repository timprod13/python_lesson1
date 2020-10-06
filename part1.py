# работа с переменными

var_float = 6/2e-2
var_bool = False
var_dict = {"Name": "Artemiy", "Surname": "Angelyuk"}
var_int = int(input("Введите число "))
print("Ваше число: %d" % var_int)
var_str = input("Введите текст ")
print("Ваш текст: %s" % var_str)
var_list = [str(var_bool), var_str, str(var_int)]
print("Коллекция: ")
print(", ".join(var_list))
