or_pass = "task1"
password = input("Введите пароль")
if password == or_pass:
    print("Пароль верен")
    name = input("Enter your name")
    print("Здравствуйте,{}.Добро пожаловать!".format(name))
    a = int(input("Введите число"))
    a = a ** 3
    print("Спасибо. Я возвел ваше число в 3-ю степень. Результат-{}".format(a))
else:
    print("Пароль неверен")
