def fact(n):
    p = 1
    for i in range(2, n + 1):
        if n != 0 or n != 1:
            p *= i
        else:
            p = 1
    yield p


for el in fact(6):
    print(el)
