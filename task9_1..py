key = int(input("Введите число от 1 до 12"))
my_dict = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль',
           8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
my_list = ("Зима", "Весна", "Лето", "Осень")
i = 0
if key <= 12 or key <= 1:
    if key == 12 or key <= 2:
        print("Ваш месяц", my_dict.get(key))
        print("Ваш сезон", my_list[i])
    else:
        if 3 <= key <= 5:
            i = i + 1
            print("Ваш месяц", my_dict.get(key))
            print("Ваш сезон", my_list[i])
        else:
            if 6 <= key <= 8:
                i = i + 2
                print("Ваш месяц", my_dict.get(key))
                print("Ваш сезон", my_list[i])
            else:
                if 9 <= key <= 11:
                    i = i + 3
                    print("Ваш месяц", my_dict.get(key))
                    print("Ваш сезон", my_list[i])
else:
    print("Вы ошиблись")
