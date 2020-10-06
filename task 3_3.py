def s_calc(a_val, b_val, c_val):
    my_set = {a_val, b_val, c_val}
    my_set.remove(min(a_val, b_val, c_val))
    return (sum(my_set))
print(s_calc(int(input("Укажите первое число: ")), int(input("Укажите второе число: ")),
             int(input("Укажите третье число: "))))