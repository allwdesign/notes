""" This is the controller module.

Accepts user input commands and delegates the presentation of the data to the
view, and the handling of the data to the model.
"""

import sys
import uuid
from datetime import datetime

import views
from model import Notes
from utils import load_from_json_file

COMMANDS = ['add', 'list', 'read', 'edit', 'del', 'exit', 'help', 'save']
NEED_ID = ['read', 'edit', 'del']


def execute_command(command: str, notes: Notes) -> None:
    """
    Execute the command received from the user.

    :param notes: Notes.
    :param command: str. The command received from the user.
    :return: None
    """

    if command in NEED_ID:
        id = views.display_need_id()

    match command:
        case 'save':
            pass
        case 'help':
            views.display_help()
        case 'add':
            tittle, msg = views.display_add()
            notes.add({'id': str(uuid.uuid4()),
                       'tittle': tittle,
                       'msg': msg,
                       'date_of_create': str(datetime.now()),
                       'date_of_update': str(datetime.now())})
        case 'list':
            views.display_notes(notes.sort('date_of_update'))
        case 'exit':
            sys.exit()
        case 'del':
            notes.delete(id)
        case 'edit':
            kwargs = views.display_edit(id)
            if kwargs:
                notes.edit(**kwargs)
        case _:
            # read
            views.display_note(notes.read(id))


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
            # We try to execute the command received from the user
            command = input('Введите команду: ').lower()
            # Validate command
            if command in COMMANDS:
                execute_command(command, notes)
            else:
                print('Неверная команда!')
        except (AttributeError, IndexError, ValueError, TypeError):
            print('Такой заметки не существует! Попробуйте еще раз.')
