class Stationery:
    atr = 'Title'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Ручка')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш')


class Handle(Stationery):
    def draw(self):
        print('Маркер')


stationery = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()
stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
