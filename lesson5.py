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
        print("3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.\n"
              " Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.\n"
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
        print("4. Создать (не программно) текстовый файл со следующим содержимым:\n"
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
                        print(new_line)
                    file_new.writelines(new_line)



