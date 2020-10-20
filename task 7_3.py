class Cell:
    def __init__(self, q):
        self.q = int(q)

    def __add__(self, other):
        return f'New cell add: {self.q + other.q}'

    def __sub__(self, other):
        sub = self.q - other.q
        return f'New cell sub: {sub} ' if sub > 0 else 'less zero'

    def __floordiv__(self, other):
        return f'New cell div: {self.q // other.q}' if other.q != 0 else 'zero'

    def __mul__(self, other):
        return f'New cell mul: {self.q * other.q}'

    def make_order(self, row):
        stars = ''
        for i in range(int(self.q / row)):
            stars += '*' * row + '\n'
        stars += '*' * (self.q % row) + '\n'
        return stars


cell = Cell(15)
new_cell = Cell(2)
print(cell + new_cell)
print(cell - new_cell)
print(cell // new_cell)
print(cell * new_cell)
print(cell.make_order(6))
