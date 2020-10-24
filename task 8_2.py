class Null:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def div(a, b):
        try:
            return a / b
        except:
            return f"b must be != null"


d = Null(100, 10)
print(Null.div(100, 0))
print(d.div(100, 10))
