# HomeWork 5.3
# Знайомимось з zip функцією, пробуємо написати свій власний zip


my_numbers = [1, 2, 3, 4, 5]
my_list = ['Manowar', 'ACDC', 'ACCEPT']
results = list(map(lambda x, y: (x, y), my_numbers, my_list))
print(results)
