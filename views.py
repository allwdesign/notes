"""This is the views module.

Presents the data to the user.
"""

from datetime import datetime
import pytz

QUANTITY = 60


def display_help():
    """
    Displays to the user what commands are in the application.

    :return: None
    """
    start_str = 'В этом приложении вы можете использовать следующие команды: '
    app_name = 'ЗАМЕТКИ'
    div_string = int((len(start_str) - len(app_name)) / 2)
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


def display_add():
    """
    Displays to the user adding interaction.

    :return: None
    """
    tittle = input("Введите заголовок заметки: ")
    print(f"заголовок = {tittle}")
    msg = input("Введите тело заметки: ")
    print(f"тело = {msg}")
    return tittle, msg


def display_note(note: dict) -> None:
    """
    Display a specific note.

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
    result = ''
    try:

        format_date = "%d-%m-%y %H:%M:%S"
        # Make a datetime object from the string
        date_cr_obj = datetime.strptime(note['date_of_create'],
                                        '%Y-%m-%d %H:%M:%S.%f')
        date_up_obj = datetime.strptime(note['date_of_update'],
                                        '%Y-%m-%d %H:%M:%S.%f')
        # Make a different output format
        date_cr_utc = pytz.utc.localize(date_cr_obj).strftime(format_date)
        date_update_utc = pytz.utc.localize(date_up_obj).strftime(format_date)

        result = (f"{QUANTITY * '-'}\n"
                  f"ID: {note['id']}\n"
                  f"Заголовок: {note['tittle']}\n"
                  f"Заметка: {note['msg']}\n"
                  f"Дата создания: {date_cr_utc}\n"
                  f"Дата обновления: {date_update_utc}\n"
                  f"{QUANTITY * '-'}")
    except TypeError:
        result = "Заметка отсутствует"
    finally:
        return result


def display_need_id():
    return input('Введите идентификатор заметки: ')
