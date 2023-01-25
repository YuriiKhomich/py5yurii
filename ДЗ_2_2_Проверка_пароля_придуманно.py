# Программа для оценки качества вводимого пароля
while True:
    pass1 = str(input("Введите свой пароль: "))
    if len(pass1) <= 8 or len(pass1) > 16:
        print("Пароль должен содержать не менее 8 и не более 16 символов!")
        continue
    if not (any(ch.isdigit() for ch in pass1)
            and not (pass1.lower() == pass1)
            and any(ch.isdigit() for ch in pass1)):
        print("Нужна как минимум, одна цифра и одна заглавная буква!")
    else:
        print("У вас четкий пароль!")
        break