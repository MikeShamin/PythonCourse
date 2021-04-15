# Задание 3: Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn

number = int(input("Введите число: "))
temp = str(number)
t1 = temp + temp
t2 = temp + temp + temp
summary = number + int(t1) + int(t2)
print("Результат равен:", summary)

