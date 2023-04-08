""" This is the controller module.

Accepts user input commands and delegates the presentation of the data to the
view, and the handling of the data to the model.
"""

import sys
import uuid
from datetime import datetime
import views
from utils import load_from_json_file
from model import Notes

COMMANDS = ['add', 'list', 'read', 'edit', 'del', 'exit', 'help', 'save']


def execute_command(command: str, notes: Notes) -> None:
    """
    Execute the command received from the user.

    :param notes: Notes.
    :param command: str
    :return: None
    """

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
            pass
        case 'exit':
            sys.exit()
        case 'del':
            pass
        case 'edit':
            pass
        case _:
            # read
            pass


def run() -> None:
    """
    Run interaction with user.

    :return: None
    """

    try:
        # Getting data with notes from a file
        notes = Notes(load_from_json_file())
        # Show the hint to the user
        views.display_help()

        while True:
            # We try to execute the command received from the user
            command = input('Введите команду: ')
            if command.lower() in COMMANDS:
                execute_command(command, notes)
    except ValueError as e:
        print(e)
