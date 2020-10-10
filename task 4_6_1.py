from itertools import count
from itertools import repeat
from itertools import islice
for i in islice(count(10),5):
    print(i)
for i in repeat("ABC",5):
    print(i)




