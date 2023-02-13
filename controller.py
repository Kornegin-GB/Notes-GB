import users_interface as ui
import os
import db


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
            db.delete_db()
            print("Все записи удалены\n")
        elif select_main_menu == 4:
            pass
        elif select_main_menu == 5:
            pass
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
