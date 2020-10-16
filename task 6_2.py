class Road:
    __length = None
    __width = None
    norm = None
    height = None
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def a(self):
        self.norm = 25
        self.height = 5
        a = (self.length * self.width * self.norm * self.height)/1000
        print(a, "тонн")

road = Road(5000, 20)
road.a()