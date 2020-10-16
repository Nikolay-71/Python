import time
from colorama import Fore, Style
class TrafficLight:
    _color = None
    _colors = ['red', 'yellow', 'green']

    def __init__(self):
        self._color = self._colors[0]

    def running(self):
        i=0
        while i<3:
            print(Fore.RED +Style.BRIGHT +self._colors[0])
            time.sleep(7)
            print(Fore.YELLOW + self._colors[1])
            time.sleep(2)
            print(Fore.GREEN +self._colors[2])
            time.sleep(2)
            print(Fore.YELLOW+self._colors[1])
            time.sleep(2)
            i+=1



traffic = TrafficLight()
traffic.running()