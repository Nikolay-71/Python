def s_calc(a_val, b_val, c_val):
    summ = a_val + b_val + c_val - min(a_val, b_val, c_val)
    return summ


print(s_calc(int(input("Укажите первое число: ")), int(input("Укажите второе число: ")),
             int(input("Укажите третье число: "))))
