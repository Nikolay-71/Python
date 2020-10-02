my_str = input("Введите слова через пробел: ")
a = my_str.split(" ")
for i, el in enumerate(a, 1):
    print("{} {:.10}".format(i, el))
