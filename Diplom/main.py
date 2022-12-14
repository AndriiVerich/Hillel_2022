# ------------------------------------------------------------------------------#
# Программа была написана такими студентами: ('Даниил Чупак', 'Андрей Верыч') ^)
# ------------------------------------------------------------------------------#

from person import *
import os


def main():
    person_list = PersonList()
    while True:
        print('-' * 30)
        print('1. Загрузить базу данных''\n2. Добавить человека', '\n3. Найти человека',
              '\n4. Удалить человека', '\n5. Сохранить',
              '\n6. Вывести базу', '\n7. Выйти')
        print('-' * 30)
        choice = input('Выберите пункт меню: ')
        # Загружаем базу данных из файла, если такой есть. Если нет, то выводим
        # сообщение об ошибке и возвращаемся в меню
        if choice == '1':
            file_name = input('Укажите имя файла: ')
            file_name = file_name + ('.xlsx' if file_name.find('xlsx') == -1 else "")
            if os.path.exists(file_name):
                person_list.load(file_name)
            else:
                print('Такого файла нет в корне')
        elif choice == '2':

            # Добавляем человека, просим ввести данные
            while True:
                name = input('Введите имя: ').title()
                if name == '':
                    print('Имя не может быть пустым')
                else:
                    break
            # Сделали проверку фамилии ради того чтобы можно было корректно удалять людей
            while True:
                surname = input('Введите фамилию: ').title()
                if surname == '':
                    print('Фамилия не может быть пустая')
                else:
                    break
            patronymic = input('Введите отчество: ').title()
            while True:
                sex = input('Введите пол (М/Ж): ').upper()
                if sex in ('М', 'Ж'):
                    break
                else:
                    print("Неправильный формат")
            while True:
                birthday = input('Введите дату рождения: ')
                try:
                    birthday = datetime.datetime.strptime(get_valid_date(birthday), '%d.%m.%Y').strftime('%d.%m.%Y')
                    break
                except ValueError:
                    print('Неверный формат даты')
            while True:
                data_death = input('Введите дату смерти: ')
                if len(data_death) == 0:
                    data_death = None
                    break
                else:
                    try:
                        data_death = datetime.datetime.strptime(get_valid_date(data_death), '%d.%m.%Y').strftime('%d.%m.%Y')
                        break
                    except ValueError:
                        print('Неверный формат даты')
            person_list.add_person(Person(name, surname, patronymic, sex, birthday, data_death))
        # Делаем запрос на поиск человека по имени, фамилии или отчеству. Если человек или люди найдены, то
        # выводим их на экран и возвращаемся в меню
        elif choice == '3':
            find = input('Введите слово по которому будет произведён поиск: ')
            person = person_list.find_persons(find)
            if person is not None:
                for i in person:
                    print(i)
            else:
                print('Человек не найден')
        elif choice == '4':
            name = input('Введите имя для удаления: ')
            surname = input('Введите фамилию для удаления: ')
            birthday = input('Введите дату рождения для удаления: ')
            if person_list.delete_person(name, surname, birthday):
                print('Человек удален')
            else:
                print('Человек не найден')
        elif choice == '5':
            while True:
                input_save = input('Сохранить в новый файл? (Да/Нет): ').upper()
                if input_save == "ДА":
                    file_name = input('Укажите имя файла: ')
                    file_name = file_name + ('.xlsx' if file_name.find('xlsx') == -1 else "")
                    person_list.save(file_name)
                    break
                elif input_save == "НЕТ":
                    person_list.save(person_list.file_name)
                    break
                else:
                    print('Нету такого варианта')
        elif choice == '6':
            person_list.get_info() if person_list.persons != [] else print('-'*30, '\nЛокальная база пуста')
        elif choice == '7':
            break
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    main()
# --------#
# The End #
