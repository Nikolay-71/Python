def s_calc():
    a = float(input("Введите  первое положительное число: "))
    b = float(input("Введите второе целое отрицательное число: "))
    if a > 0 and b.is_integer():
        n = 0
        while n <= abs (b):
            a = a * a
            n = n + 1
            sub = 1 / a
            break
        return sub
    else:
        return "Введите первое положительное число и второе целое отрицательное число"


print(s_calc())
