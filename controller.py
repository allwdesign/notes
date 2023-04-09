""" This is the controller module.

Accepts user input commands and delegates the presentation of the data to the
view, and the handling of the data to the model.
"""

import sys
import uuid
from datetime import datetime

import views
from model import Notes
from utils import load_from_json_file, save_to_file

OTHER = ['add', 'exit', 'help']
NEED_ID = ['read', 'edit', 'del']
NEED_NOTES = ['list', 'save']
COMMANDS = OTHER + NEED_ID + NEED_NOTES


def execute_command(command: str, notes: Notes) -> None:
    """
    Execute the command received from the user.

    :param notes: Notes.
    :param command: str. The command received from the user.
    :return: None
    """

    response = ''
    id = ''
    note = dict()

    if (command in NEED_NOTES) or (command in NEED_ID):
        # Only if the collection of notes is complete can we delete,
        # read, edit the note, save or list the notes.
        if not notes:
            raise Exception

    if command in NEED_ID:
        id = views.display_need_id()
        note = notes.read(id)

    match command:
        case 'exit':
            if notes and views.display_save_before_exit():
                save_to_file(notes.get_notes())
            sys.exit()
        case 'save':
            save_to_file(notes.get_notes())
            print('Успешное сохранение в файл.')
        case 'help':
            views.display_help()
        case 'list':
            views.display_notes(notes.sort('date_of_update'))
        case 'add':
            tittle, msg = views.display_add()
            notes.add({'id': str(uuid.uuid4()),
                       'tittle': tittle,
                       'msg': msg,
                       'date_of_create': str(datetime.now()),
                       'date_of_update': str(datetime.now())})
            response = 'добавлена'
        case 'del':
            views.display_delete()
            notes.delete(note)
            response = 'удалена'
        case 'edit':
            kwargs = views.display_edit()
            if kwargs:
                notes.edit(note, **kwargs)
                response = 'обновлена'
        case _:
            # read
            views.display_note(note)

    if response:
        views.display_result(response)


def run() -> None:
    """
    Run interaction with user.

    :return: None
    """

    # Getting data with notes from a file
    notes = Notes(load_from_json_file())

    # Show the hint to the user
    views.display_help()
    while True:
        try:
            # Get user input command
            command = views.display_get_user_command()
            # Validate command
            if command in COMMANDS:
                # We try to execute the command received from the user
                execute_command(command, notes)
            else:
                raise ValueError('Неверная команда!')
        except (AttributeError, IndexError, TypeError):
            print('Такой заметки не существует! Попробуйте еще раз.')
        except ValueError as error:
            print(error.args[0])
        except Exception:
            print(('Пока нет заметок. Можете добавить заметку с промощью'
                   ' команды add.'))
