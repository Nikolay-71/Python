def s_calc(a_val, b_val):
    if a_val > 0 and b_val.is_integer():
        sub = a_val ** b_val
        return sub
    else:
        return "Введите первое положительное число и второе целое отрицательное число"


print(s_calc(float(input("Введите  положительное число: ")), float(input("Введите целое отрицательное число: "))))
