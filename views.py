"""This is the views module.

Presents the data to the user.
"""

from datetime import datetime

QUANTITY = 60


def display_help():
    """
    Displays to the user what commands are in the application.

    :return: None
    """
    start_str = 'В этом приложении вы можете использовать следующие команды: '
    app_name = 'ЗАМЕТКИ'
    div_string = int((len(start_str) - len(app_name)) / 2)
    print(len(start_str) * '-')
    print(div_string * ' ', app_name, div_string * ' ')
    print(len(start_str) * '-')
    print(start_str)
    print(('add  - Добавить заметку\n'
           'read - Просмотреть заметку\n'
           'list - Вывести на экран список заметок\n'
           'edit - Редактировать\n'
           'del  - Удалить\n'
           'help - Вызвать справку по командам\n'
           'save - Сохранить заметки в файл'))
    print(len(start_str) * '-')


def display_get_user_command() -> str:
    """
    Displays to the user adding command interaction.

    :return: str.
    """
    print()
    user_input = input('Введите команду: ').lower()
    print()
    return user_input


def display_notes(sorted_notes: list) -> None:
    """
    Shows a list of notes sorted by date of update in descending order.

    :param sorted_notes: list.
    :return: None
    """
    if not sorted_notes:
        raise Exception

    print(f"{QUANTITY * '-'}")
    print(f'Всего заметок: {len(sorted_notes)}.')
    for note in sorted_notes:
        # note is dict
        print(__make_formatted_data(note))
    print(f"{QUANTITY * '-'}")


def display_add() -> tuple:
    """
    Displays to the user adding interaction.

    :return: tuple. tittle, msg
    """
    print(f"{QUANTITY * '-'}")
    print(f"Добавление Заметки")
    print(f"{QUANTITY * '-'}")
    tittle = input("Введите заголовок заметки: ")
    msg = input("Введите тело заметки: ")

    return tittle, msg


def display_edit() -> dict:
    """
    Displays to the user edit interaction.

    :return: dict
    """
    res = dict()
    variants = ['t', 'm', 'a', 'c']

    print(f"{QUANTITY * '-'}")
    print(f"Редактирование Заметки")
    print(f"{QUANTITY * '-'}")
    print(("Опции редактирования:\n"
           "t - Заголовок\n"
           "m - Тело заметки\n"
           "a - Всё\n"
           "с - Отменить редактирование"))
    print(f"{QUANTITY * '-'}")

    choice = input("Выбeрите, что хотите отредактировать: ").lower()
    print(f"{QUANTITY * '-'}")

    if choice not in variants:
        raise ValueError('Неверная команда!')

    match choice:
        case 't':
            new_tittle = input("Введите заголовок заметки: ")
            res.update({'tittle': new_tittle})
        case 'm':
            new_msg = input("Введите тело заметки: ")
            res.update({'msg': new_msg})
        case 'a':
            new_tittle = input("Введите заголовок заметки: ")
            new_msg = input("Введите тело заметки: ")
            res.update({'tittle': new_tittle, 'msg': new_msg})
        case _:
            print("Отмена редактирования")
    return res


def display_note(note: dict) -> None:
    """
    Display to the user a specific note.

    :param note: dict. Note.
    :return: None
    """
    print(__make_formatted_data(note))


def __make_formatted_data(note: dict) -> str:
    """
    User-friendly information format.

    :param note: dict. Information about note.
    :return: str. Formatted string.
    """
    format_date = "%d-%m-%y %H:%M:%S"
    # Make a datetime object from the string
    date_cr_obj = datetime.strptime(note['date_of_create'],
                                    '%Y-%m-%d %H:%M:%S.%f')
    date_up_obj = datetime.strptime(note['date_of_update'],
                                    '%Y-%m-%d %H:%M:%S.%f')
    # Make a User-friendly output format
    date_cr_utc = date_cr_obj.strftime(format_date)
    date_update_utc = date_up_obj.strftime(format_date)

    return (f"{QUANTITY * '-'}\n\n"
            f"ID: {note['id']}\n"
            f"Заголовок: {note['tittle']}\n"
            f"Заметка: {note['msg']}\n"
            f"Дата создания: {date_cr_utc}\n"
            f"Дата обновления: {date_update_utc}\n\n"
            f"{QUANTITY * '-'}")


def display_need_id():
    """
    Displays a prompt for a note ID.

    :return: str. User input ID.
    """
    id = input('Введите ID заметки: ')
    print()
    return id


def display_result(msg: str) -> None:
    """
    Displays a message to the user about successfully completed commands.

    :param msg: str. Message for successfully pattern.
    :return: None
    """
    print()
    print(f'Заметка успешно {msg}.')
    print()


def display_delete() -> None:
    """
    Displays to the user delete interaction.

    :return: None
    """
    print(f"{QUANTITY * '-'}")
    print(f"Удаление Заметки")
    print(f"{QUANTITY * '-'}")


def display_save_before_exit() -> bool:
    """
    Displays to the user save interaction before user exit from app.

    :return: bool. Whether the user needs to save notes to a file.
    """
    flag = False
    variants = ['y', 'n']
    print(f"{QUANTITY * '-'}")
    print(f"Выход из приложения Заметки")
    print(f"{QUANTITY * '-'}")
    print(("Опции для сохранения:\n"
           "y - Да\n"
           "n - Нет"))
    print(f"{QUANTITY * '-'}")
    choice = input("Хотите ли вы сохранить заметки в файл: ").lower()
    print(f"{QUANTITY * '-'}")

    if choice not in variants:
        raise ValueError('Неверная команда!')

    if choice == 'y':
        flag = True

    return flag
