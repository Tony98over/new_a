number=int(input("Введите число:"))

def summa_n():
    count=0
    for sum in range(0,number+1):
        count+=sum

    print("Сумма от 1 до ", number, ':',count)
    return count

def summa2():
    total=0
    for sum2 in range(0,summa_n()+1):
        total+=sum2
    print(total)
print("Сумма от 1 до ",number,':',summa_n())
print("Сумма от 1 до ",summa_n(),':',summa2())



summa_n()