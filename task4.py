a = int(input("Введите целое число:"))
b = a % 10
a = a // 10
while a > 0:
    if b < a % 10:
        b = a % 10
        a = a // 10
    else:
        a = a // 10
print("Наибольшая цифра: {}".format(b))
