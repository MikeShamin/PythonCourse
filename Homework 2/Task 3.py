"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

# Реализация через list

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
month = int(input("Введите номер месяца: "))
if month == 12 or month == 12 or month == 2:
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])
else:
    print("Указан несуществующий месяц")

# Реализация через dict

seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
dict_month = int(input("Введите номер месяца: "))
if dict_month == 12 or dict_month == 1 or dict_month == 2:
    print(seasons_dict.get(1))
elif dict_month == 3 or dict_month == 4 or dict_month == 5:
    print(seasons_dict.get(2))
elif dict_month == 6 or dict_month == 7 or dict_month == 8:
    print(seasons_dict.get(3))
elif dict_month == 9 or dict_month == 10 or dict_month == 11:
    print(seasons_dict.get(4))
else:
    print("Указан несуществующий месяц")
