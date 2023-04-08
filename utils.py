"""This is the utils module.

Module for storing information between program launches.
"""

from os import path
import json

# '/your_absolute_path_here/notes.json'
JSON_FILE = path.abspath('notes.json')


def create_json_file():
    with open(JSON_FILE, 'w', encoding='utf-8') as outfile:
        json.dump([],
                  outfile,
                  ensure_ascii=False,
                  indent=4,
                  default=str,
                  separators=(',', ': '))


def load_from_json_file() -> list:
    """
    Load notes from file if file exists otherwise create empty JSON file.

    :return: list with notes
    """
    if not path.isfile(JSON_FILE):
        create_json_file()

    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        notes = json.load(f)
    print('Заметки загружены из файла', notes)
    return notes
