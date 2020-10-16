class Worker:
    name = None
    surname = None
    position = None
    wage = None
    bonus = None

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def full(self):
        return self.name + " " + self.surname

    def salary(self):
        self.__income = {'profit': self.wage, 'bonus': self.bonus}
        return sum(self.__income.values())


pers = Position('Николай', 'Чернов', 'директор', 15000, 1000)
print(pers.full(), pers.position, pers.salary())
