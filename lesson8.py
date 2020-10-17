def days(day, num_day):
    """вспомогательная функция определяющая какое из двух чисел больше"""
    
    if day > num_day:
        return num_day
    else:
        return day


def isinteger(text):
    """функция проверяющая введено ли число, если нет просит ввести его еще раз"""
    while True:
        numbers = input(text)
        try:
            if not numbers.isdigit():
                raise MyError("Вы ввели не число.")
        except MyError as err_1:
            print(err_1)
        else:
            return numbers


class Data:
    """Класс принимающий дату в виде строки валидирующий ее и возвращающий ее ввиде чисел, содержит два метода функции
    типов classmethod и staticmethod"""
    def __init__(self, data):
        print("Атрибут функции: ", data)
        self.data = Data.metod_one(data)
        print("День, месяц, год - после обработки первым методом: ", self.data)
        print("Скорректированная дата после валидации вторым методом: ", Data.metod_two(self.data[0], self.data[1],
                                                                                        self.data[2]))

    @classmethod
    def metod_one(cls, data_one):
        """Преобразовывает строку в числа день, месяц, год"""
        str_1 = data_one.split('-')
        day = int(str_1[0])
        month = int(str_1[1])
        year = int(str_1[2])
        return day, month, year

    @staticmethod
    def metod_two(day, month, year):
        """валидирует дату и возвращает ее"""
        if day < 0:
            day_new = 1
        elif day > 28:
            if month == 2:
                if year % 4 == 0:
                    day_new = days(day, 29)
                else:
                    day_new = days(day, 28)
            elif month == 4 or month == 6 or month == 9 or month == 11:
                day_new = days(day, 30)
            else:
                day_new = 31
        else:
            day_new = day

        if month < 0:
            month_new = 1
        elif month > 12:
            month_new = 12
        else:
            month_new = month
        if year > 2020:
            year_new = 2020
        elif year < 0:
            year_new = 0
        else:
            year_new = year
        data_new = [day_new, month_new, year_new]
        return data_new


class MyError(Exception):
    """Класс для выведения сообщения об ошбике"""
    def __init__(self, txt):
        self.txt = txt


class Sklad:
    """Класс склад хранит данные об остатках типа оргтехники и какой она модели, содержит две функции одна для
     добавления на склад, вторая для перемещения со склада.
     В качестве аргумента функции принимают объект класса Orgtakhnika """

    def __init__(self):
        self.my_dict = {}

    def add(self, objects, numbers):
        """добавляем объект на склад"""
        new_dict = {objects.model: numbers}
        # есть ли данный тип в словаре
        if objects.types in self.my_dict:
            i = False
            # перебираем элементы списка
            for el in range(len(self.my_dict[objects.types])):
                # Если в списке уже есть такой ключ, то нужно пометить, что он найден и увеличить его значение
                if objects.model in self.my_dict[objects.types][el].keys():
                    i = True
                    self.my_dict[objects.types][el][objects.model] += numbers
            # если совпадений не было найдено добавляем элемент в список
            if i is False:
                self.my_dict[objects.types].append(new_dict)
        # если данного типа нет нужно добавить элемент
        else:
            self.my_dict[objects.types] = [new_dict]

    def rashod(self, objects, numbers):
        """убирает со склада объект"""
        # есть ли данный тип в словаре
        if objects.types in self.my_dict:
            i = False
            # перебираем элементы списка
            for el in range(len(self.my_dict[objects.types])):
                # Если в списке уже есть такой ключ, то помечаем что были совпадения и проверяем достаточно ли кол-во
                # для списания
                if objects.model in self.my_dict[objects.types][el].keys():
                    i = True
                    if self.my_dict[objects.types][el][objects.model] > numbers:
                        self.my_dict[objects.types][el][objects.model] -= numbers
                    else:
                        # выдаем под остаток и удаляем запись
                        if self.my_dict[objects.types][el][objects.model] != 0:
                            print("На складе нет указанного количеста данной модели, выдадим только то что есть: ",
                                  self.my_dict[objects.types][el][objects.model])
                        self.my_dict[objects.types].pop(el)
            # если совпадений не было найдено выводи об этом сообщение
            if i is False:
                print("На складе нет данной модели")
        # если данного типа нет выводим сообщение
        else:
            print("На складе нет данного типа оборудования")


class Orgtekhnika:
    """Родительский класс для классов Printer, Skaner, Kserox"""

    def __init__(self, types, model, price):
        self.model = model
        self.price = price
        self.types = types


class Printer(Orgtekhnika):
    """Дочерний класс для класса Orgtekhnika"""

    def __init__(self, model, price, resurs):
        super().__init__("printer", model, price)
        self.resurs = resurs


class Skaner(Orgtekhnika):
    """Дочерний класс для класса Orgtekhnika"""

    def __init__(self, model, price, colors_bit):
        super().__init__("skaner", model, price)
        self.num_colors_scan = colors_bit


class Kserox(Orgtekhnika):
    """Дочерний класс для класса Orgtekhnika"""

    def __init__(self, model, price, speed):
        super().__init__("kserox", model, price)
        self.copy_speed_minute = speed


class KomplNum:
    """Класс комплексного числа, перегрузка методов сложения и умножения"""
    def __init__(self, d_num, mn_num):
        self.d_num = d_num
        self.mn_num = mn_num

    def __str__(self):
        if self.mn_num > 0:
            return f"z={self.d_num}+i{self.mn_num}"
        elif self.mn_num < 0:
            return f"z={self.d_num}-i{-self.mn_num}"
        else:
            return f"z={self.d_num}"

    def __add__(self, other):
        """сложение комплексных чисел"""
        return KomplNum(self.d_num + other.d_num, self.mn_num + other.mn_num)

    def __mul__(self, other):
        """умножение комплексных чисел"""
        a1 = self.d_num
        a2 = other.d_num
        b1 = self.mn_num
        b2 = other.mn_num
        return KomplNum(a1*a2 - b1*b2, a1*b2 + a2*b1)


while True:
    zadanie = int(isinteger("\nВведите номер задания, для выхода введите 0: "))
    if zadanie == 0:
        break
    elif zadanie == 1:
        print("Задание 1: Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки\n"
              "формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,\n"
              "должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».\n"
              "Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года\n"
              "(например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.\n")
        a = Data('32-02-2020')
        print(Data.metod_one)
        print(a.metod_one)
        print(Data.metod_two)
        print(a.metod_two)
    elif zadanie == 2:
        print("Задание 2: Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.\n"
              "Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве\n"
              "делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.\n")
        inp_num_1 = int(isinteger("Введите делимое число: "))
        inp_num_2 = int(isinteger("Введите делитель: "))

        try:
            if inp_num_2 == 0:
                raise MyError("Вы ввели ноль. На ноль делить нельзя")
        except ValueError:
            print("Вы ввели не число")
        except MyError as err:
            print(err)
        else:
            print(f"{inp_num_1}/{inp_num_2} = {inp_num_1 / inp_num_2}")
    elif zadanie == 3:
        print("Задание 3: Создайте собственный класс-исключение, который должен проверять содержимое списка\n"
              "на наличие только чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать\n"
              "у пользователя данные и заполнять список. Класс-исключение должен контролировать типы данных элементов\n"
              "списка.\n"
              "Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не\n"
              "остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный\n"
              "список выводится на экран.\n"
              "Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе\n"
              "пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список\n"
              "только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число)\n"
              "и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.\n")
        spisok = []
        print("Для окончания скрипта нужно ввести 'stop'")
        while True:
            number = input("Введите число: ")
            if number == "stop":
                print(spisok)
                break
            try:
                if not number.isdigit():
                    raise MyError("Вы ввели не число.")
            except MyError as err:
                print(err)
            else:
                spisok.append(number)
    elif zadanie == 4:
        print("Задание 4: Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.\n"
              "А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные\n"
              "типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для\n"
              "приведенных типов.\n"
              "В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.\n")
        printer_1 = Printer("HP", 5000, 6000)
        printer_2 = Printer("Canon", 4000, 4000)
        skaner_1 = Skaner("Mustec", 2000, 24)
        skaner_2 = Skaner("Canon", 3000, 16)
        kserox_1 = Kserox("HP", 10000, 60)
        kserox_2 = Kserox("Canon", 12000, 50)

        print(printer_1.types)
        print(skaner_1.types)
        print(kserox_1.types)
    elif zadanie == 5:
        print("Задание 5: Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники\n"
              "на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании\n"
              "и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,\n"
              "например словарь.\n")
        # определяем 2 склада склад и офис
        sklad_1 = Sklad()
        office_1 = Sklad()
        # определяем объекты дочерних классов Orgtekhnika
        printer_1 = Printer("HP", 5000, 6000)
        printer_2 = Printer("Canon", 4000, 4000)
        skaner_1 = Skaner("Mustec", 2000, 24)
        skaner_2 = Skaner("Canon", 3000, 16)
        kserox_1 = Kserox("HP", 10000, 60)
        kserox_2 = Kserox("Canon", 12000, 50)
        # добавляем их на склад
        sklad_1.add(printer_1, 10)
        sklad_1.add(printer_2, 20)
        sklad_1.add(skaner_1, 10)
        sklad_1.add(skaner_2, 20)
        sklad_1.add(printer_1, 100)
        # выводим остатки на складах
        print("Склад: ", sklad_1.my_dict)
        print("Офис: ", office_1.my_dict)
        # создаем объект для перемещения
        office_printer = Printer("HP", 3000, 6000)
        # перемещаем со склада в офис
        sklad_1.rashod(office_printer, 10)
        office_1.add(office_printer, 10)
        # выводим остатки по складам
        print("Склад: ", sklad_1.my_dict)
        print("Офис: ", office_1.my_dict)
    elif zadanie == 6:
        print("Задание 6: Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем\n"
              "данных."
              "Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый\n"
              "тип данных."
              "Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,\n"
              "изученных на уроках по ООП.\n")
        models = ['HP', 'Canon', 'Samsung']
        sklad_1 = Sklad()
        print("Склад: ", sklad_1.my_dict)
        print("1. Принтер\n"
              "2. Сканер\n"
              "3. Ксерокс")
        num_1 = int(isinteger("Выберите тип оргтехники: "))

        if num_1 == 1:
            item = 1
            for elem in models:
                print(f"{item} {elem}")
                item += 1
            num_2 = int(isinteger("Введите номер модели: "))
            num_3 = int(isinteger("Введите количество поступившее на склад: "))
            printer_1 = Printer(models[num_2 - 1], 5000, 6000)
            sklad_1.add(printer_1, num_3)
        elif num_1 == 2:
            item = 1
            for elem in models:
                print(f"{item} {elem}")
                item += 1
            num_2 = int(isinteger("Введите номер модели: "))
            num_3 = int(isinteger("Введите количество поступившее на склад: "))
            scaner_1 = Skaner(models[num_2 - 1], 5000, 6000)
            sklad_1.add(scaner_1, num_3)
        elif num_1 == 3:
            item = 1
            for elem in models:
                print(f"{item} {elem}")
                item += 1
            num_2 = int(isinteger("Введите номер модели: "))
            num_3 = int(isinteger("Введите количество поступившее на склад: "))
            kserox_1 = Kserox(models[num_2 - 1], 5000, 6000)
            sklad_1.add(kserox_1, num_3)
        else:
            print("Такой тип объекта не предусмотрен программой")
        print("Склад: ", sklad_1.my_dict)
    elif zadanie == 7:
        print("7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,\n"
              "реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,\n"
              "создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.\n"
              "Проверьте корректность полученного результата.\n")
        # инициализируем два комплексных числа и выводим их на экран
        num_1 = KomplNum(3, 5)
        num_2 = KomplNum(2, -2)
        print(num_1)
        print(num_2)
        # проводим их сложение
        print("Сложение комплексных чисел: ", num_1 + num_2)
        # проводим их перемножение
        print("Умножение комплексных числе: ", num_1 * num_2)
    else:
        print("Такого задания нет")
