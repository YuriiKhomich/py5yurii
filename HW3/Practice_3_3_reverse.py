#Написать программу, которая выводит саму себя задом наперед
f = open('Practice_3_3_reverse.py', encoding='utf-8-sig')
spisok = f.read().rstrip().split('\n')
spisok = spisok[::-1]
for line in spisok:
    print(line[::-1].lstrip())
f.close()

