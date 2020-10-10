from itertools import cycle
from itertools import count
for el in count(7):
    if el > 15:
        i = 0
        a = cycle("ABC")
        while i < 7:
    print(next(a))
    i += 1
    else:
        print(el)
