def s_calc(f_val, s_val):
    try:
        sub = f_val / s_val
        return sub
    except ZeroDivisionError:
        return "Введите корректные данные"


print(s_calc (float(input("Укажите первое число: ")), float(input("Укажите второе число: "))))
