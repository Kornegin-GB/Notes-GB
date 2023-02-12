import users_interface as ui
import os


def run():
    """Модуль запуска программы"""
    while True:
        select_main_menu = ui.main_menu()
        if select_main_menu == 1:
            os.system("cls")
            select_record_processing(ui.menu_operation())
        elif select_main_menu == 2:
            pass
        elif select_main_menu == 3:
            pass
        elif select_main_menu == 4:
            pass
        elif select_main_menu == 5:
            pass
        else:
            os.system("cls")
            print("Работа с программой завершена\n")
            exit()


def select_record_processing(item):
    """ Обработка меню работы с записью """
    pass


def processing_import_menu(menu, path):
    """ Обработка меню импорта """
    pass


def import_file(path, expansion):
    """ Обработка файла для импорта """
    pass
