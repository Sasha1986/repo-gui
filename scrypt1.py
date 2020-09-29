# Скрипт с параметрами, итератор генерирующий целые числа, начиная с указанного
# в первом задании выводим целые числа, начиная с 3, а при достижении числа 15 завершаем цикл
from sys import argv
from itertools import count

script, first  = argv

for el in count(int(first)):
    if el > 15:
        break
    else:
        print(el)
