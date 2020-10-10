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
    elif
    else:
        print("Такого задания нет")
