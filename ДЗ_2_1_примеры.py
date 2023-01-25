print('Пример 1:')
print ("Give it to me!")
number = int(input("Enter the amount of cash: "))
if (number >= 100):
    print ("Thanks, man!")
elif ((number > 10) and (number < 100)):
    print ("OK :(")
else:
    print ("WHAAAAT????")
if (number > 1000):
    print ("!!!!WOOOOWWWW!!!")


print("Пример 2: ")
test = True
result = 'Test is True' if test else 'Test is False'
print ('ttt' if test else 'fff')
print(result)

