def circle():
    number = int(input("Введите число:"))
    print("Какое действие хотите совершить?\n1-вывести сумму его цифр\n2-вывести максимальную цифру\n3-вывести минимальную цифру")
    action = int(input())
    if action == 1:
        summ(number)
    elif action == 2:
        max(number)
    elif action == 3:
        min(number)
    else:
        print("Неккоректный ввод.Повторите попытку")
    circle()


def summ(number):
    sum = 0
    while number > 0:
        a = number % 10
        sum += a
        number //= 10
    print(sum)


def max(number):
    sum = 0
    b = number % 10
    while number > 0:
        a = number % 10
        number //= 10
        if a >= b:
            sum = a
    print(sum)


def min(number):
    sum = 0
    b = number % 10
    while number > 0:
        a = number % 10
        number //= 10
    if a <= b:
        sum = a
    print(sum)


circle()
