my_list = list(input("Введите данные"))
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        a = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = a
        i = i + 2
else:
    i = 0
    while i < len(my_list) - 1:
        a = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = a
        i = i + 2
print(my_list)
