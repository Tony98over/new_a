def summa_n():
    summ=0
    number=int(input("Введите число:"))
    for total in range(1,number+1):
        summ+=total
    print("Я знаю что сумма чисел от 1", "до", number, "равно",summ )

summa_n()

#Готово