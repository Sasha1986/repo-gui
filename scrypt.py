# Скрипт с параметрами
from sys import argv

script, first, second, third = argv

zarplata = int(first) * int(second) + int(third)
print("Sallary = ", zarplata)

