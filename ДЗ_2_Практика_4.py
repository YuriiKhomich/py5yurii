#Ввести число, вывести его разряды и их множители.
number = int(input("Введите число: "))
Mnoj = len(str(number))      # Вычисляем общее количество множителей
Kol_mnoj = 0                 # Счетчик множителей
a = 10
c = 1
while Kol_mnoj < Mnoj:
    a1 = number % a
    a2 = int(str(a1)[0])
    print(a2, "*", c)
    c = c*10
    a = a*10
    Kol_mnoj += 1