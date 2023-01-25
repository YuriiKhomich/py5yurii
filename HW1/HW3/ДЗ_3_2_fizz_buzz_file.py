# Написать fizzbuzz для 20 троек чисел, которые записаны в файл.
# Читаете из файла первую строку, берете из нее числа,
# считаете для них fizzbuzz, выводите, повторяете со всеми остальными строками.

f = open('fizz_buzz.txt')
for line in f:
    word_list = line.split()
    num_list = []
    for word in word_list:
        if word.isnumeric():
            num_list.append(int(word))
    print(num_list)
    fizz = int(num_list[0])
    buzz = int(num_list[1])
    numb = int(num_list[2])
    result = ''
    for x in range(1, numb+1):
        if not x % (fizz) and x % (buzz):
            result += "F"
        if not x % (buzz) and x % (fizz):
            result += "B"
        if not x % (fizz) and not x % (buzz):
            result += "FB"
        if x % (fizz) and x % (buzz):
            result += str(x)
        result += " "
    print(f'{result}\n')
f.close()


