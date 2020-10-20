from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, size):
        self.size = size

    @property
    def total(self):
        return f'Total: {coat.size / 6.5 + 0.5 + 2 * suit.size + 0.3:.1f}'

    @abstractmethod
    def calc(self):
        return '!!!'


class Coat(Clothes):

    def calc(self):
        return f'Coat: {self.size / 6.5 + 0.5:.1f} '



class Suit(Clothes):

    def calc(self):
        return f'Suit: {2 * self.size + 0.3:.1f} '


coat = Coat(40)
suit = Suit(4)

print(coat.calc())
print(suit.calc())
print(coat.total)
print(suit.total)
