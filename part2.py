# расчёт секунд в чч:мм:сс

time = int(input("Введите время в секундах "))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60
print("Полученный результат: %02d:%02d:%02d" % (hours, minutes, seconds))
