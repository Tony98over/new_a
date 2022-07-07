x = int(input("Введите число:"))


def float_point(x):
    b = -1
    while x > 0:
        x //= 10
        b += 1
    return b


a = x / 10 ** float_point(x)
print(a)
print("x=", a, "*10**", float_point(x))
print("adw")

print("vkad")
