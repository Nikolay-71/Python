a = int(input("Введите сумму выручки:"))
b = int(input("Введите сумму издержек:"))
loss = b - a
profit = a - b
r = 100 * (profit / a)
if b > a:
    print("Ваш убыток равен: {}".format(loss))
else:
    p = int(input("Введите количество сотрудников:"))
    ren = profit / p
    print("Ваша прибыль: {},ваша рентабельность:{:.0f}%,прибыль на одного сотрудника:{:.0f} ".format(profit, r, ren))
