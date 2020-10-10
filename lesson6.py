import time

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
