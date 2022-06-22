def search():
    text = input("Введите текст:")
    letter = input("Какую букву ищем?:")
    number = input("Какую цифру ищем?:")
    let = 0
    num = 0

    for symbol in text:
        if symbol == letter:
            let += 1
        if symbol == number:
            num += 1
    print("Количество цифр ", number, ":", num)
    print("Количество букв ", letter, ":", let)


while True:
    search()

# good
