# FIZZ/BUZZ with List comprehensions


# У вас есть три числа, они вводятся из консоли. Первое число
# называется fizz, второе называется buzz. До третьего необходимо
# досчитать от единицы. Считая, надо выводить число. Если число
# кратно fizz - надо выводить F вместо числа. Если число кратно buzz -
# надо выводить B вместо числа. Если число кратно и fizz и buzz, надо
# выводить FB. И так - пока не будет достигнуто третье введенное число.
#
# Пример условия и результата:
# Введены числа 2, 5, 18
# Вывод должен быть таким:
# 1 F 3 F B F 7 F 9 FB 11 F 13 F B F 17 F

fizz = int(input("Введите первое число (fizz): "))
buzz = int(input("ВВедите второе число (buzz): "))
numb = int(input("Введите третье число: "))
result = ["F" if not x % fizz and x % buzz
           else "B" if not x % buzz and x % fizz
           else "FB" if not x % fizz and not x % buzz
           else x for x in range(1, numb+1)]
my_str = ' '.join(str(x) for x in result)
print(my_str)

