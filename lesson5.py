from random import randint
import json

while True:
    zadanie = int(input("\nВведите номер задания, для выхода введите 0: "))
    print("")
    if zadanie == 0:
        break
    elif zadanie == 1:
        print("1. Создать программно файл в текстовом формате, записать в него построчно данные,\n"
              "вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.")
        file = open("test.txt", "w")
        while True:
            string = input("Введите строку: ")
            file.write(string + '\n')
            if string == "":
                file.close()
                break
        with open("test.txt") as f_obj:
            for line in f_obj:
                print(line)
    elif zadanie == 2:
        print("Задание 2: Создать текстовый файл (не программно), сохранить в нем несколько строк,\n"
              "выполнить подсчет количества строк, количества слов в каждой строке.")
        with open("test2.txt") as file:
            line_num = 0
            for line in file:
                line_num += 1
                words = line.split(" ")
                word_num = 0
                for word in words:
                    word_num += 1
                print(f"В строке {line_num} количетсво слов: {word_num}.")
            print(f"Количество строк в файле: {line_num}.")
    elif zadanie == 3:
        print("Задание 3: Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину\n"
              "их окладов. Определить, кто из сотрудников имеет оклад менее 20тыс., вывести фамилии этих сотрудников.\n"
              "Выполнить подсчет средней величины дохода сотрудников.")
        print("Оклад менее 20000 имеют: ")
        salary = 0
        number = 0
        with open("test3.txt") as file:
            for line in file:
                words = line.split(" ")
                salary += int(words[1])
                number += 1
                if int(words[1]) < 20000:
                    print(words[0])
        print(f"Средняя зарплата: {salary / number}")
    elif zadanie == 4:
        print("Задание 4: Создать (не программно) текстовый файл со следующим содержимым:\n"
              "One — 1\n"
              "Two — 2\n"
              "Three — 3\n"
              "Four — 4\n"
              "Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.\n"
              "При этом английские числительные должны заменяться на русские.\n"
              "Новый блок строк должен записываться в новый текстовый файл.")
        with open("zadanie4_new.txt", "w") as file_new:
            with open("zadanie4.txt") as file:
                for line in file:
                    words = line.split(" ")
                    new_line = []
                    for word in words:
                        if word == "One":
                            new_line.append("Один")
                        elif word == "Two":
                            new_line.append("Два")
                        elif word == "Three":
                            new_line.append("Три")
                        elif word == "Four":
                            new_line.append("Четыре")
                        else:
                            new_line.append(f' {word}')
                    file_new.writelines(new_line)
    elif zadanie == 5:
        print("Задание 5: Создать (программно) текстовый файл, записать в него программно набор чисел,\n"
              "разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.")
        numbers = []
        item = 0
        summ = 0
        while item < 10:
            if item == 9:
                numbers.append(f"{randint(1, 1000)}")
            else:
                numbers.append(f"{randint(1,1000)} ")
            item += 1
        with open("test5.txt", "w") as file:
            file.writelines(numbers)
        with open("test5.txt", "r") as file:
            for line in file:
                words = line.split(" ")
                for word in words:
                    num = int(word)
                    summ += num
        print("Сумма чисел в файле: ", summ)
    elif zadanie == 6:
        print("Задание 6: Необходимо создать (не программно) текстовый файл, где каждая строка описывает\n"
              "учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету\n"
              "и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.\n"
              "Сформировать словарь, содержащий название предмета и общее количество занятий по нему.\n"
              "Вывести словарь на экран. Примеры строк файла:\n"
              "Информатика: 100(л) 50(пр) 20(лаб).\n"
              "Физика: 30(л) — 10(лаб)\n"
              "Физкультура: — 30(пр) —\n"
              "Пример словаря:\n"
              "{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}")
        subjects = {}
        with open("zadanie6.txt", "r") as file:
            for line in file:
                summ = 0
                words = line.split(":")
                words_new = words[1].split(" ")
                for word in words_new:
                    num = word.split("(")
                    for num_1 in num:
                        if num_1.isdigit():
                            summ += int(num_1)
                subjects[words[0]] = summ
        print("Решение:\n", subjects)
    elif zadanie == 7:
        print("Задание 7: Создать (не программно) текстовый файл, в котором каждая строка должна содержать\n"
              "данные о фирме: название, форма собственности, выручка, издержки.\n"
              "Пример строки файла: firm_1 ООО 10000 5000.\n"
              "Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.\n"
              "Если фирма получила убытки, в расчет средней прибыли ее не включать.\n"
              "Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со\n"
              "средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).\n"
              "Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].\n"
              "Итоговый список сохранить в виде json-объекта в соответствующий файл.\n"
              # Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]"
              "Подсказка: использовать менеджеры контекста.")
        firma = []
        firms_income = 0
        num_firms = 0
        firms = {}
        with open("zadanie7.txt", "r") as file:
            for line in file:
                firma = line.split(" ")
                income = int(firma[2]) - int(firma[3])
                if income >= 0:
                    firms_income += income
                    num_firms += 1
                firms[firma[0]] = income
        spisok = [firms, {"average_profit": firms_income / num_firms}]
        print(spisok)
        with open("my_file.json", "w") as write_f:
            json.dump(spisok, write_f)
