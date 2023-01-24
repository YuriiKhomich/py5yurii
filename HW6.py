#Завдання 3
Візьміть файл, в якому є багато англійських слів у рядках. Порахуйте частоту зустрічі
кожного слова та видрукуйте відсортовано.

import json
document_text = open('text.txt', 'r')
text_string = document_text.read()
total_count = {}


def calc_word(word):
    if word in total_count:
        total_count[word] += 1
    else:
        total_count[word] = 1


list(map(lambda x: calc_word(''.join(filter(str.isalpha, x.lower()))), text_string.split()))
print(json.dumps(total_count, indent=2, sort_keys=True))
