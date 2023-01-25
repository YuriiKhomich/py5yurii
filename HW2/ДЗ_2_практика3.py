# Ввести число, вывести все его делители.
number = int(input("Введите число: "))
i = 1
while i <= number:
    if not number % i:
        print("делитель ", i)
    i += 1
