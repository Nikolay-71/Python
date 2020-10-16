class Cars:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return "Go"

    def stop(self):
        return "Stop"

    def turn(self, direction):
        return "Turn to the " + direction

    def show_speed(self, speed):
        return "Speed is " + speed


class TownCar(Cars):
    civil = None

    def __init__(self, name, speed, color, civil=None):
        super().__init__(name, speed, color)
        self.civil = civil

    def show_speed(self, speed):
        if self.speed > 60:
            return "Speed limit exceed. Speed is " + speed
        return "Speed is OK - " + speed


class SportCar(Cars):
    civil = None

    def __init__(self, name, speed, color, civil=None):
        super().__init__(name, speed, color)
        self.civil = civil


class WorkCar(Cars):
    civil = None

    def __init__(self, name, speed, color, civil=None):
        super().__init__(name, speed, color)
        self.civil = civil

    def show_speed(self, speed):
        if self.speed > 40:
            return "Speed limit exceed. Speed is " + speed
        return "Speed is OK - " + speed


class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)


opel = TownCar('Opel', 90, 'black')
print(opel.name, opel.color, opel.is_police)
print(opel.go(), "", opel.show_speed("90"), '', opel.turn('left'), '', opel.stop())
police = PoliceCar('Plimuth', 100, 'red')
print(police.name, police.color, police.is_police)
print(police.go(), "", police.show_speed("100"), "", police.turn('left'), '', police.stop())
