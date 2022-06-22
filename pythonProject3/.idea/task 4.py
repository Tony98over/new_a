number = int(input("Введите число:"))
b=0

while number>0:
    a=number%10
    number=number//10
    b=b*10
    b=b+a
print(b)

#good