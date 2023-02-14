import users_interface as ui
import os
import db
import model_csv as csv


def run():
    """Модуль запуска программы"""
    os.system("cls")
    while True:
        select_main_menu = ui.main_menu()
        if select_main_menu == 1:
            os.system("cls")
            select_record_processing(ui.menu_operation())
        elif select_main_menu == 2:
            ui.show_result(db.read_db())
        elif select_main_menu == 3:
            os.system("cls")
            serch_db = db.search_db(ui.search_notes())
            ui.show_result(serch_db)
        elif select_main_menu == 4:
            os.system("cls")
            db.delete_db()
            print("Все записи удалены\n")
        elif select_main_menu == 5:  # Загрузить
            os.system("cls")
            processing_import_menu(
                ui.menu_import(),
                ui.selecting_file().split(".")
            )
            os.system("cls")
            print("База данных обнавлена успешно\n")
        elif select_main_menu == 6:  # Выгрузить
            os.system("cls")
            export_file(ui.menu_export())
        else:
            exit()


def select_record_processing(item):
    """ Обработка меню работы с записью """
    if item == 1:
        data = ui.entry_record_data()
        db.insert_one_entry_db(data)
        os.system("cls")
        print("Запись добавлена\n")
    elif item == 2:
        os.system("cls")
        ui.show_result(db.read_db())
        if (len(db.read_db()) > 0):
            db.update_one_entry_db(
                ui.up_del_user(db.read_db(), "изменения"),
                ui.entry_record_data()
            )
            os.system("cls")
            print("Запись изменина\n")
    elif item == 3:
        os.system("cls")
        ui.show_result(db.read_db())
        if (len(db.read_db()) > 0):
            db.delete_one_entry(ui.up_del_user(db.read_db(), "удаления"))
        os.system("cls")
        print("Запись удалена\n")
    else:
        run()


def export_file(item):
    """Модуль сохранения данных в файл"""
    if item == 1:
        data_db = db.read_db()
        csv.file_csv_export(data_db, ui.selecting_file())
        os.system("cls")
        print("Файл сохранен успешно\n")
    elif item == 2:
        os.system("cls")
        serch_db = db.search_db(ui.search_notes())
        ui.show_result(serch_db)
        item_yes_no = ui.yes_no()
        if item_yes_no == 1:
            csv.file_csv_export(serch_db, ui.selecting_file())
            os.system("cls")
            print("Файл сохранен успешно\n")
        else:
            run()
    else:
        run()


def processing_import_menu(menu, path):
    """ Обработка меню импорта """
    try:
        data = csv.file_csv_import(path[0])
        if menu == 1:
            db.delete_db()
            db.insert_db(data)
        else:
            db.insert_db(data)
    except IndexError:
        print("Не правильное имя файла")
