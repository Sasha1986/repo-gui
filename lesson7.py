from abc import ABC, abstractmethod

while True:
    zadanie = int(input("\nВведите номер задания, для выхода введите 0: "))
    print("")
    if zadanie == 0:
        break
    elif zadanie == 1:
        print("Задание 1: Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса\n"
              "(метод __init__()), который должен принимать данные (список списков) для формирования матрицы.\n"
              "Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной\n"
              "схемы. Примеры матриц вы найдете в методичке. Следующий шаг — реализовать перегрузку метода __str__()\n"
              "для вывода матрицы в привычном виде. Далее реализовать перегрузку метода __add__() для реализации\n"
              "операции сложения двух объектов класса Matrix (двух матриц).\n"
              "Результатом сложения должна быть новая матрица."
              "Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки\n"
              "первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.")
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        matrix2 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        class Matrix:
            def __init__(self, matrix_1):
                self.matrix_1 = matrix_1

            def __str__(self):
                matr = str()

                for el in self.matrix_1:
                    ryad = str()

                    for item in el:
                        ryad += f"{item} "

                    matr += f"{ryad}\n"

                return matr

            def __add__(self, other):
                matrix_add = []
                matrix_row = []
                for i in range(len(self.matrix_1)):
                    matrix_row.clear()
                    for j in range(len(self.matrix_1[i])):
                        matrix_row.append(self.matrix_1[i][j] + other.matrix_1[i][j])
                    matrix_add.append(matrix_row[:])
                return Matrix(matrix_add)

        mat_1 = Matrix(matrix)
        mat_2 = Matrix(matrix2)
        print(mat_1 + mat_2)
    elif zadanie == 2:
        print("Задание 2: Реализовать проект расчета суммарного расхода ткани на производство одежды.\n"
              "Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.\n"
              "К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:\n"
              "размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.\n"
              "Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),\n"
              "для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.\n"
              "Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:\n"
              "реализовать абстрактные классы для основных классов проекта, проверить на практике работу\n"
              "декоратора @property.")

        class Clothes(ABC):
            @abstractmethod
            def Consumption(self, size):
                self.size = size
                self.consumption = self.size
                return self.consumption

            def __str__(self):
                return f"Расход ткани: {self.consumption}м2"

            def __add__(self, other):
                return self.consumption + other.consumption

        class Coat(Clothes):

            def Consumption(self, size=0):
                self.size = size
                self.consumption = self.size / 6.5 + 0.5
                return self.consumption

            @property
            def size(self):
                return self.__size

            @size.setter
            def size(self, size):
                if size < 20:
                    self.__year = 20
                elif size > 60:
                    self.__size = 60
                else:
                    self.__size = size

            @property
            def MyCoat(self):
                return "Расход ткани на мое пальто 3.5м2"

        class Suit(Clothes):
            def Consumption(self, height=0.0):
                self.height = height
                self.consumption = self.height * 2 + 0.5
                return self.consumption

        coat_1 = Coat()
        coat_2 = Coat()
        coat_3 = Coat()
        suit_1 = Suit()

        coat_1.Consumption(100)
        coat_2.Consumption(60)
        coat_3.Consumption(40)
        suit_1.Consumption(1.7)

        print("Пальто1 100 размер", coat_1)
        print("Пальто2 60 размер", coat_2)
        print("Пальто3 40 размер", coat_3)
        print(suit_1)
        print("Суммарный расход ткани: ", coat_1+suit_1)
        print(coat_1.MyCoat)
    elif zadanie == 3:
        print("Задание 3: Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.\n"
              "В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).\n"
              "В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),\n"
              "вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться\n"
              "только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление\n"
              "клеток, соответственно. В методе деления должно осуществляться округление значения до целого числа.\n"
              "Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек\n"
              "исходных двух клеток. Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если\n"
              "разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.\n"
              "Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение\n"
              "количества ячеек этих двух клеток. Деление. Создается общая клетка из двух. Число ячеек общей клетки\n"
              "определяется как целочисленное деление количества ячеек этих двух клеток. В классе необходимо\n"
              "реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.\n"
              "Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку\n"
              "вида *****\ n *****\ n*****..., где количество ячеек между \ n равно переданному аргументу. Если ячеек\n"
              "на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.\n"
              "Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()\n"
              "вернет строку: *****\ n*****\ n**. Или, количество ячеек клетки равняется 15,\n"
              "количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\ n*****\ n*****.\n"
              "Подсказка: подробный список операторов для перегрузки доступен по ссылке.")

        class Cell:
            def __init__(self, quantity):
                self.quantity = quantity

            def __str__(self):
                return str(self.quantity)

            def __add__(self, other):
                return self.quantity + other.quantity

            def __sub__(self, other):
                if (self.quantity - other.quantity) > 0:
                    return self.quantity - other.quantity
                else:
                    return "Вычитаемых ячеек больше чем имеющихся"

            def __mul__(self, other):
                return self.quantity * other.quantity

            def __truediv__(self, other):
                if self.quantity < other.quantity:
                    return "В первой клетке ячеек больше, чем во второй"
                else:
                    return round(self.quantity // other.quantity)

            def make_order(self, number_cell):
                self.number_cell = int(number_cell)
                if self.quantity > number_cell:
                    rezult = "*" * self.number_cell
                    whole = self.quantity // self.number_cell
                    remains = self.quantity % self.number_cell
                    rezult = rezult + "\n"
                    rezult = rezult * whole
                    if remains > 0:
                        rezult += "*" * remains + "\n"
                    return rezult + "\n"
                elif self.quantity == None:
                    print("Ячейки отсутствуют")
                else:
                    return "*" * self.quantity + "\n"

        cell_1 = Cell(5)
        cell_2 = Cell(3)
        cell_3 = Cell(6)
        cell_4 = Cell(4)
        cell_5 = Cell(2)
        cell_6 = Cell(12)
        cell_7 = Cell(15)
        cell_8 = Cell(36)

        print(f"{cell_1} + {cell_2} = {cell_1 + cell_2}")
        print(f"{cell_2} - {cell_5} = {cell_2 - cell_5}")
        print(f"{cell_5} - {cell_1} = {cell_5 - cell_1}")
        print(f"{cell_5} * {cell_2} = {cell_5 * cell_2}")
        print(f"{cell_4} / {cell_3} = {cell_4 / cell_3}")
        print(f"{cell_4} / {cell_5} = {cell_4 / cell_5}")
        print(f"{cell_3} / {cell_4} = {cell_3 / cell_4}")

        print(cell_1.make_order(6))
        print(cell_6.make_order(5))
        print(cell_7.make_order(5))
        print(cell_8.make_order(10))


    else:
        print("Такого задания нет")
