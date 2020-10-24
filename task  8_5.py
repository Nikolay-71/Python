class Number:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        return f'add_z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'mul_z = {self.a * other.a - self.b * other.b} + {self.b * other.a + self.a * other.b} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = Number(5, 6)
z_2 = Number(1, 8)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
