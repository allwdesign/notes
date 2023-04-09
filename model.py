"""This is the model module.

Manages the collection of notes.
"""

from datetime import datetime


class Notes:
    """
    Class for working with a collection of notes.
    """

    def __init__(self, data: list):
        self.collection = data

    def __str__(self):
        return f"Notes: {self.collection}"

    def __repr__(self):
        return f"Notes({self.collection})"

    def __bool__(self):
        return bool(self.collection)

    def __len__(self):
        return len(self.collection)

    def __get_note_by_id(self, id: str) -> dict:
        """
        Get note by given ID.

        :param id: str. The note ID we want to get.
        :return: dict. The note we want to get.
        """
        return list(filter(lambda x: x['id'] == id, self.collection))[0]

    def get_notes(self) -> list:
        """
        Get sorted collections of notes by date_of_update field in descending
        order.

        :return: list
        """
        return self.collection

    def add(self, note: dict) -> None:
        """
        Add the note to collection.

        :param note: dict. Note object.
        :return: None
        """
        self.collection.append(note)

    def read(self, id: str) -> dict:
        """
        Read the note from collection.

        :param id: str. The note ID we want to read.
        :return: dict
        """
        return self.__get_note_by_id(id)

    def edit(self, note: dict, **kwargs) -> None:
        """
        Edit the note from collection.

        :param note: dict. The note we want to update.
        :param kwargs: Can contain keys: the tittle, the msg or both.
        :return: None
        """
        kwargs.update({'date_of_update': str(datetime.now())})
        note.update(kwargs)

    def delete(self, note: dict) -> None:
        """
        Delete the note from collection.

        :param note: dict. The note we want to delete.
        :return: None
        """
        self.collection.remove(note)

    def sort(self, field: str) -> list:
        """
        Sorts the list of notes by the given field. In descending order.

        :param field: str. The field by which we will sort the notes.
        :return: list
        """
        sorted = []

        for x in self.collection:
            i = 0
            for y in sorted:
                if x[field] >= y[field]:
                    break
                i += 1
            sorted[i:i] = [x]
        return sorted
