from mygroup import groupmates



def print_students(students):
    try:
        average_mark = float(input('Введите средний балл, по которому будет производиться фильтрация: '))
    except ValueError:
        print('Введено неверное значение!')
        return 1

    # Создать список студентов, средний балл которых выше введённого с клавиатуры
    result = []
    for student in students:
        if sum(student['marks']) / len(student['marks']) >= average_mark:
            result.append(student)

    # Вывод на экран созданного списка
    print(f'Студенты, средний балл которых выше {average_mark}'.ljust(75))
    if not result:
        print('Нет таких студентов!')
        return 1

    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in result:
        print(student["name"].ljust(15),
              student["surname"].ljust(10),
              str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(20))


if __name__ == '__main__':
    print_students(groupmates)
