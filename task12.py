my_dict = {name: 'a', price: 'b'}
while input("Желаете ввести новый продукт? да/нет: ") == 'да':
    a = input("Введите название продукта: ")
    b = input("Введите цену: ")
       my_list.append(tuple([a, b]))
print(my_list)
analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
            analitics[feature_key] = [feature_value]
print(analitics)
