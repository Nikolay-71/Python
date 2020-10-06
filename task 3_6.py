while True:
    a = input("Введите число или s для остановки программы: ")
    b = a.split(" ")
    sum_1 = 0
    for word in b:
        if word == 's':
            break
            print(f"Сумма {sum_1}. Программа остановлена")
            value = float(word)
            sum_1 += value
        print(sum_1)
