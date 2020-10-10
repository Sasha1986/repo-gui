import time
from random import randint

while True:
    zadanie = int(input("\nВведите номер задания, для выхода введите 0: "))
    print("")
    if zadanie == 0:
        break
    elif zadanie == 1:
        print("Задание 1: Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)\n"
              "и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение\n"
              "светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный)\n"
              "составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.\n"
              "Переключение между режимами должно осуществляться только в указанном порядке(красный, желтый, зеленый)\n"
              "Проверить работу примера, создав экземпляр и вызвав описанный метод.\n"
              "Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить\n"
              "соответствующее сообщение и завершать скрипт.")
        class TrafficLight:
            color = ('red', 'yellow', 'green')

            def running(self, red, yellow, green):
                while True:
                    print(TrafficLight.color[0])
                    time.sleep(red)
                    print(TrafficLight.color[1])
                    time.sleep(yellow)
                    print(TrafficLight.color[2])
                    time.sleep(green)
        a = TrafficLight()
        a.running(7, 2, 5)
    elif zadanie == 2:
        print('Задание 2: Реализовать класс Road (дорога), в котором определить атрибуты: length (длина),\n'
              'width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.\n'
              'Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия\n'
              'всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного\n'
              'кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.\n'
              'Например: 20м * 5000м * 25кг * 5см = 12500 т')
        class Road():
            maasa2 = 0
            def _massa(self, _length, _width):
                massa2 = _length * _width * 25 * 5 / 1000
                print(f"Масса полотна: {massa2}тонн")
        a = Road()
        a._massa(1000, 200)
    elif zadanie == 3:
        print("Задание 3: Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,\n"
              "position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,\n"
              "содержащий элементы: оклад и премия, например, {wage: wage, bonus: bonus}.\n"
              "Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы\n"
              "получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).\n"
              "Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,\n"
              "проверить значения атрибутов, вызвать методы экземпляров).")

        class Worker:
            dict_income = [{'wage': 10000, 'bonus': 2000}, {'wage': 20000, 'bonus': 5000},{'wage': 10000, 'bonus': 5000}]
            def __init__(self, name, surname, position, _income):
                self.name = name
                self.surname = surname
                self.position = position
                self.income = self.dict_income[_income]

        class Position(Worker):
            def __init__(self, name,surname,position,_income):
                super().__init__(name,surname,position,_income)
            def get_full_name(self):
                full_name =  self.name + " "+ self.surname
                print(f"Сотрудник: {full_name}")
            def get_total_income(self):
                total_income = self.income['wage'] + self.income['bonus']
                print(f"Доход с учетом премии: {total_income}")

        men_1 = Position('Vasya','Bykov','Director',1)
        men_2 = Position('Петр','Иванов','Грузчик',0)
        men_3 = Position("Галина","Громова","Бухгалетр",2)

        men_1.get_full_name()
        men_1.get_total_income()
        men_2.get_full_name()
        men_2.get_total_income()
        men_3.get_full_name()
        men_3.get_total_income()
    elif zadanie == 4:
        print("Задание 4: Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:\n"
              "speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),\n"
              "которые должны сообщать, что машина поехала, остановилась, повернула (куда).\n"
              "Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.\n"
              "Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.\n"
              "Для классов TownCar и WorkCar переопределите метод show_speed.\n"
              "При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении\n"
              "скорости.\n"
              "Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,\n"
              "выведите результат. Выполните вызов методов и также покажите результат.")
        class Car:
            def __init__(self, speed, color, name, is_police=False):
                self.speed = speed
                self.color = color
                self.name = name
                self.is_police = is_police
            def go(self):
                if self.speed > 0:
                    print("Машина поехала")
            def stop(self):
                if self.speed == 0:
                    print("Машина остановилась")
            def turn(self):
                where_turn = randint(1,2)
                if self.speed == 0:
                    print("Maшина стоит")
                else:
                    if where_turn == 1:
                        print("Машина повернула направо")
                    elif where_turn == 2:
                        print("Машина повернула налево")
                    elif where_turn == 3:
                        print("Машина едет задом")
                    else:
                        print("Машина движется прямо")
            def show_speed(self):
                print(f"Текущая скорость: автомбиля {self.name} - {self.speed}км/ч")
        class TownCar(Car):
            def show_speed(self):
                super().show_speed()
                if self.speed > 60:
                    print("Скорость превышена")
        class SportCar(Car):
            pass
        class WorkCar(Car):
            def show_speed(self):
                super().show_speed()
                if self.speed > 40:
                    print("Скорость превышена")
        class PoliceCar(Car):
            pass

        car_1 = TownCar(61,"white",'Audi')
        car_11 = TownCar(50,"red","Mersedes")
        car_12 = TownCar(0,"blue","Lada")
        car_2 = SportCar(120,"black","Ferrari")
        car_3 = WorkCar(45,"yellow","Fiat")
        car_31 = WorkCar(35,"grenn","Skania")
        car_4 = PoliceCar(70,"white-blue","УАЗ",True)

        print(car_1.speed)
        print(car_2.color)
        print(car_3.name)
        print(car_4.is_police)
        print(car_11.is_police)
        car_3.show_speed()
        car_31.show_speed()
        car_1.show_speed()
        car_11.show_speed()
        car_4.show_speed()
        car_1.go()
        car_12.go()
        car_1.stop()
        car_12.stop()
        car_1.turn()
        car_12.turn()
    elif zadanie == 5:
        print("Задание 5: Реализовать класс Stationery (канцелярская принадлежность).\n"
              "Определить в нем атрибут title (название) и метод draw (отрисовка).\n"
              "Метод выводит сообщение “Запуск отрисовки.”\n"
              "Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).\n"
              "В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы\n"
              "должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет\n"
              "описанный метод для каждого экземпляра.")
        class Stationery:
            def __init__(self, title=None):
                self.title = title
            def draw(self):
                print("Запуск отрисовки")
        class Pen(Stationery):
            def draw(self):
                print("Отрисовка ручкой")
        class Pencil(Stationery):
            def draw(self):
                print("Отрисовка карандашом")
        class Handle(Stationery):
            def draw(self):
                print("Отрисовка маркером")

        stationery_1 = Stationery()
        stationery_2 = Pen()
        stationery_3 = Pencil()
        stationery_4 = Handle()

        stationery_1.draw()
        stationery_2.draw()
        stationery_3.draw()
        stationery_4.draw()


