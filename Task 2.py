# Задание 2: Преобразование времени в секундах в формт чч:мм:сс

sec = int(input("Введите время в секундах: "))
hours = sec // 3600
minutes = (sec - hours * 3600) // 60
seconds = sec % 60
print(hours, 'час', minutes, 'мин', seconds, 'сек')
