# Ввести число, вывести все его делители.
# reliz 2

number = int(input("Введите число: "))
result = [x for x in range(1, number+1) if not number % x]
print(result)

#Вариант 2. Функция.

def delitel(number):
    result = {1, number}
    for delitel in range(2, number // 2 + 1):
      if not number % delitel:
         result.add(delitel)
    return sorted(result)

