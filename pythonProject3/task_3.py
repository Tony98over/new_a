print('Задача 3. Число наоборот 2')

# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример:

# Введите первое число: 102
# Введите второе число: 123


# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225

number_One = int(input('Введите первое число:'))
number_Two = int(input('Введите второе число:'))


def one(number_One):
    a = 0
    while number_One > 0:
        i = number_One % 10
        number_One //= 10
        a *= 10
        a += i
    return a


def two(number_Two):
    a = 0
    while number_Two > 0:
        i = number_Two % 10
        number_Two //= 10
        a *= 10
        a += i
    return a


print("Сумма: ", number_Two + number_One)
print("Сумма наоборот: ", one(number_One) + two(number_Two))

# good
