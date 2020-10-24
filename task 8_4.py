class Store:

    def __init__(self, name, price, q, *args):
        self.name = name
        self.price = price
        self.q = q
        self.store_2 = []
        self.store = []
        self.new = {'Модель ': self.name, 'Цена': self.price, 'Количество': self.q}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.q}'

    def input(self):

        try:
            a = input(f'Введите модель  ')
            b = int(input(f'Введите цену  '))
            c = int(input(f'Введите количество  '))
            my_dic = {'Модель': a, 'Цена': b, 'Количество': c}
            self.store.append(my_dic)
            print(f'{self.store}')

        except:
            return f'Введите корректные значения'

        s = input(f"Если хотите закончить нажмите-s  ").lower()
        if s == 's':
            self.store_2.append(self.store)
            print(f'Сводная номенклатура -\n {self.store_2}')
            return f'Окончание работы'
        else:
            return Store.input(self)


class Printer(Store):
    def __init__(self, name, price, q, ser_nom):
        super().__init__(name, price, q)
        self.ser_nom = ser_nom

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.q} серия {self.ser_nom}'


class Scanner(Store):
    def __init__(self, name, price, q, ser_nom):
        super().__init__(name, price, q)
        self.ser_nom = ser_nom

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.q} серия {self.ser_nom}'


class Copier(Store):
    def __init__(self, name, price, q, ser_nom):
        super().__init__(name, price, q)
        self.ser_nom = ser_nom

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.q} серия {self.ser_nom}'


unit_1 = Printer('hp', 2000, 5, 1015)
unit_2 = Scanner('Canon', 1200, 5, 1020)
unit_3 = Copier('Xerox', 1500, 1, 1530)
print(unit_1.input())
print(unit_1)
print(unit_2)
print(unit_3)
