from itertools import count
from itertools import cycle

for el in count(7):
    if el > 15:
        break
    else:
        print(el)
i = 0
a = cycle("ABC")
while i < 7:
    print(next(a))
    i += 1
