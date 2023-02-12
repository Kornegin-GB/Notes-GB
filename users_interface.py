import os
import datetime as dt


def main_menu():
    """ Главное меню программы """
    name_main_menu = "Гланое меню"
    menu = [
        "Обработать заметки",
        "Прочитать заметки",
        "Удалить заметки",
        "Загрузить заметки из файла",
        "Выгрузить заметки в файл",
        "Выход",
    ]
    return selecting_item(menu, name_main_menu)


def menu_operation():
    """ Меню работы с записью """
    name_operation_menu = "Меню записи"
    menu = [
        "Создать запись",
        "Изменить запись",
        "Удалить запись",
    ]
    return selecting_item(menu, name_operation_menu)


def menu_import():
    """ Меню работы с записью """
    name_import_menu = "Меню импорта"
    menu = [
        "Загрузить файл заменой заметок",
        "Загрузить файл с добавлением заметок",
    ]
    return selecting_item(menu, name_import_menu)


def selecting_item(date_menu, name):
    """ Модуль обработки выбора меню """
    os.system("cls")
    while True:
        try:
            print(name)
            for item in enumerate(date_menu, 1):
                print(item[0], item[1])
            item_number = int(input("Выберите пункт меню: "))
            if 1 <= item_number <= len(date_menu):
                return item_number
            else:
                raise ValueError
        except ValueError:
            os.system("cls")
            print("Выберите правильный пункт меню\n")


def entry_record_data():
    """ Модуль ввода данных записи """
    header = input("Введите заголовок: ")
    text = input("Введите текст заметки: ")
    date_recording = dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(date_recording)
    record = [header, text, date_recording]
    return record
