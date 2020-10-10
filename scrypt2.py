# итератор, повторяющий элементы некоторого списка, определенного заранее.
from itertools import cycle


с = 0
for el in cycle("Hello world! "):
    if с > 25:
        break
    print(el)
    с += 1
