print("Введите кооррдинаты")
x = float(input("X:"))
y = float(input("Y:"))
print("Укажите шаг сетки:")
step = int(input())

x = round(x)
y = round(y)
if x > step * -1 and x < step:
    print("Монетка где-то рядом")
else:
    print("Монетки в области нет")

# good
