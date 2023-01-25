# Написать программу, которая выводит сама себя
f = open('Practice_3_2_self_output.py', encoding='utf-8-sig')
for line in f:
    print(line.rstrip())
f.close()
