def Day(day, num_day):
    if day > num_day:
        return num_day
    else:
        return day


class Data:
    def __init__(self, data):
        print("Атрибут функции: ", data)
        self.data = Data.metod_one(data)
        print("День, месяц, год - после обработки первым методом: ", self.data)
        print("Скорректированная дата после валидации вторым методом: ", Data.metod_two(self.data[0], self.data[1],
                                                                                        self.data[2]))

    @classmethod
    def metod_one(cls, data_one):
        str_1 = data_one.split('-')
        day = int(str_1[0])
        month = int(str_1[1])
        year = int(str_1[2])
        return day, month, year

    @staticmethod
    def metod_two(day, month, year):
        if day < 0:
            day_new = 1
        elif day > 28:
            if month == 2:
                if year % 4 == 0:
                    day_new = Day(day, 29)
                else:
                    day_new = Day(day, 28)
            elif month == 4 or month == 6 or month == 9 or month == 11:
                day_new = Day(day, 30)
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
    def __init__(self, txt):
        self.txt = txt


class Sklad:
    def __init__(self):
        self.type = []
        self.name = []
        self.count = []
        self.price = []

    def priem(self, name, number, price):
        pass

    def rashod(self):
        pass


class Orgtekhnika:
    def __init__(self, type, model, price):
        self.model = model
        self.price = price
        self.type = type


class Printer(Orgtekhnika):
    def __init__(self, model, price, resurs):
        super().__init__("printer", model, price)
        self.resurs_cartridg = resurs


class Skaner(Orgtekhnika):
    def __init__(self, model, price, colors_bit):
        super().__init__("skaner", model, price)
        self.num_colors_scan = colors_bit


class Kserox(Orgtekhnika):
    def __init__(self, model, price, speed):
        super().__init__("kserox", model, price)
        self.copy_speed_minute = speed


while True:
    zadanie = int(input("\nВведите номер задания, для выхода введите 0: "))
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
        inp_num_1 = int(input("Введите делимое число: "))
        inp_num_2 = int(input("Введите делитель: "))

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

        print(printer_1.type)

    else:
        print("Такого задания нет")
