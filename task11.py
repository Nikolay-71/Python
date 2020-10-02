my_list = [7, 6, 5, 3, 3, 2, 1]
a = int(input("Введите целое положительное число"))
my_list.append(a)
my_list.sort()
final = my_list[::-1]
print(final)
