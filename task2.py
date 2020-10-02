time = int(input("Введите время в секундах"))
hour = time // 3600
m = (time - hour * 3600) // 60
sec = (time - hour * 3600 - m * 60)
print("Ваше время {} ч {} мин {} сек".format(hour, m, sec))
