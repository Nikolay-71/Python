sum_1 = 0
while True:
    a = input("Введите число или s для остановки программы: ")
    b = a.split(" ")
    for word in b:
        if word != "s":
            try:

                value = float(word)
                sum_1 += value
            except:
                 pass
        else:
            print("Программа остановлена. Сумма - {}".format(sum_1))
            exit()
    print("Сумма - {}".format(sum_1))
