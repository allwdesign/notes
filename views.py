"""This is the views module.

Presents the data to the user.
"""


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
    print(('add - Добавить заметку\n'
           'read - Просмотреть заметку\n'
           'list - Вывести на экран список заметок\n'
           'edit - Редактировать\n'
           'del - Удалить\n'
           'help - Вызвать справку по командам\n'
           'save - Сохранить заметки в файл'))
    print(len(start_str) * '-')
