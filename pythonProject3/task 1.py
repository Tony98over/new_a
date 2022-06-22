print("Введите число")
number=int(input())

def summa_n(number):
    count=0
    for summa in range(1,number+1):

        count=summa+summa
        count+=summa
        print("Я знаю, что сумма чисел от 1 до ",number," равна ",count)

summa_n(number)


