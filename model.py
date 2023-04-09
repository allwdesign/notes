"""This is the model module.

Manages the collection of notes.
"""

from datetime import datetime


class Notes:
    """
    Class for working with a collection of notes.
    """

    def __init__(self, data: list):
        self.collections = data

    def __str__(self):
        return f"Notes: {self.collections}"

    def __repr__(self):
        return f"Notes({self.collections})"

    def __get_note_by_id(self, id: str):
        return list(filter(lambda x: x['id'] == id, self.collections))[0]

    def get_notes(self) -> list:
        """
        Get collections of notes.

        :return: list
        """
        return self.collections

    def add(self, note: dict) -> None:
        """
        Add the note to collection.

        :param note: dict. Note object.
        :return: None
        """
        self.collections.append(note)
        print(note['id'])

    def read(self, id: str) -> dict:
        """
        Read the note from collection.

        :param id: str. Note id.
        :return: dict
        """
        return self.__get_note_by_id(id)

    def edit(self, **kwargs) -> None:
        """
        Edit the note from collection.

        :param kwargs: Can be id, tittle, msg.
        :return: None
        """
        note = self.__get_note_by_id(kwargs['id'])
        kwargs.update({'date_of_update': str(datetime.now())})
        note.update(kwargs)

    def delete(self, id: str) -> None:
        """
        Delete the note from collection.

        :param id: str. Note id.
        :return: None
        """
        note = self.__get_note_by_id(id)
        self.collections.remove(note)

    def sort(self, field: str) -> list:
        """
        Sorts the list of notes by the given field.

        :param field: str. The field by which we will sort the notes.
        :return: list
        """
        sorted = []

        for x in self.collections:
            i = 0
            for y in sorted:
                if x[field] >= y[field]:
                    break
                i += 1
            sorted[i:i] = [x]
        return sorted
