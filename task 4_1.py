from sys import argv
try:
    script_name, vir, stavka, prem = argv
    for i in argv:
        i.isnumeric() > 0
        salary = float(vir) * float(stavka) + float(prem)
    print("Ваша зарплата:", salary)
except ValueError:
    print("Некорректный ввод")
