my_list = [7, 6, 5, 3, 2, 1]
a = int(input("Введите целое положительное число"))
b = my_list.count(a)
for el in my_list:
    if b > 0:
        i = my_list.index(a)
        my_list.insert(i + b, a)
        if a > el:
            r = my_list.index(el)
            my_list.insert(r, a)
        else:
            my_list.append(a)
print(my_list)
