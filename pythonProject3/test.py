summa = float(input("Введите сумму кредита:"))
year = float(input("На сколько лет выдан?:"))
procent = float(input("Сколько процентов годовых?:"))
procent_2=procent/100
n=0
ostatok=summa




def srednee(summa,procent):
    cof=summa/100*procent
    return cof
def anuitet(procent,year):
    cof_a=(procent_2*(1+procent_2)**year)/((1+procent_2)**year-1)
    return cof_a
def body(summa,cof_a,cof):
    body_credit=ostatok*cof_a-cof
    return body_credit


for period in range(1,4):
    cof_a = (procent_2 * (1 + procent_2) ** year) / ((1 + procent_2) ** year - 1)
    cof = summa / 100 * procent
    body_credit = ostatok * cof_a - cof

    n+=1
    print('\n'"Период: ",n,'\n')
    print('Остаток долга на начало периода:',summa)
    print('Выплачено процентов:',srednee(summa,procent))
    print('Выплачено тела кредита:',body(summa,cof_a,cof))

    summa -= body_credit

print('=================================================')

new_years=int(input('На сколько лет продляется договор?'))
new_procent=float(input('Увеличение ставки до: '))
new_procent_2=new_procent/100
while ostatok!=body(summa,cof_a,cof):
    cof_a = (new_procent_2 * (1 + new_procent_2) ** new_years+year) / ((1 + new_procent_2) ** new_years+year - 1)
    cof = summa / 100 * new_procent
    body_credit = ostatok * cof_a - cof

    n+=1
    print('\n'"Период: ",n,'\n')
    print('Остаток долга на начало периода:',summa)
    print('Выплачено процентов:',srednee(summa,new_procent))
    print('Выплачено тела кредита:',body(summa,cof_a,cof))

    summa -= body_credit


