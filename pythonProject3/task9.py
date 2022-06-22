
summa = float(input("Введите сумму кредита:"))
year = float(input("На сколько лет выдан?:"))
procent = float(input("Сколько процентов годовых?:"))
procent_2 = procent / 100
n = 0
ostatok = summa

cof = summa / 100 * procent

cof_a = (procent_2 * (1 + procent_2) ** year) / ((1 + procent_2) ** year - 1)

for period in range(1, 4):
    cof_a = (procent_2 * (1 + procent_2) ** year) / ((1 + procent_2) ** year - 1)
    cof = summa / 100 * procent
    body_credit = ostatok * cof_a - cof

    n += 1
    print('\n'"Период: ", n, '\n')
    print('Остаток долга на начало периода:', summa)
    print('Выплачено процентов:', cof)
    print('Выплачено тела кредита:', body_credit)

    summa -= body_credit

print(' ', '\n', '=================================================', '\n'' ')

new_years = int(input('На сколько лет продляется договор?'))
new_procent = float(input('Увеличение ставки до: '))
new_procent_2 = new_procent / 100
Cof = summa / 100 * new_procent
Cof_a = (new_procent_2 * (1 + new_procent_2) ** year + new_years) / ((1 + new_procent_2) ** year + new_years - 1)
i = 0
while i < 5:
    Cof_aof_a = (new_procent_2 * (1 + new_procent_2) ** new_years + year) / (
                (1 + new_procent_2) ** new_years + year - 1)
    Cofof = summa / 100 * new_procent
    body_credit = ostatok * Cof_a - Cof

    i += 1
    print('\n'"Период: ", i, '\n')
    print('Остаток долга на начало периода:', summa)
    print('Выплачено процентов:', Cof)
    print('Выплачено тела кредита:', body_credit)

    summa -= body_credit
